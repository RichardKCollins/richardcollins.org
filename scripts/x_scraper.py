#!/usr/bin/env python3
"""
Playwright-based X (Twitter) Article & Long-Form Post Scraper.
Supports:
  - Persistent login session (.browser_data)
  - Scanning profile /articles tab to build a manifest
  - Batch export to formatted Markdown with YAML frontmatter
  - Resume capability (skips already exported articles)
"""

import argparse
import asyncio
import json
import os
import re
import sys
import time
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse

from bs4 import BeautifulSoup
import markdownify
import yaml

from playwright_stealth import Stealth

stealth = Stealth()

ROOT_DIR = Path(__file__).resolve().parent.parent
BROWSER_DATA_DIR = ROOT_DIR / ".browser_data"
CONTENT_DIR = ROOT_DIR / "content" / "x-articles"
MANIFEST_FILE = CONTENT_DIR / "manifest.json"

DEFAULT_HANDLE = "RichardKCollin2"
USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
)
CHROMIUM_ARGS = [
    "--disable-blink-features=AutomationControlled",
    "--no-sandbox",
    "--disable-infobars",
    "--disable-dev-shm-usage",
    "--disable-browser-side-navigation",
    "--disable-features=IsolateOrigins,site-per-process",
]


def slugify(text: str) -> str:
    """Generate a filesystem-safe slug from text."""
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_-]+", "-", text)
    return text.strip("-")[:60] or "untitled"


async def get_browser_context(p, headless: bool = False):
    """Launch or attach to persistent browser context with stealth applied."""
    BROWSER_DATA_DIR.mkdir(parents=True, exist_ok=True)
    context = await p.chromium.launch_persistent_context(
        user_data_dir=str(BROWSER_DATA_DIR),
        headless=headless,
        args=CHROMIUM_ARGS,
        user_agent=USER_AGENT,
        viewport={"width": 1280, "height": 900},
        ignore_default_args=["--enable-automation"],
    )
    return context


async def prepare_page(page):
    """Apply stealth evasion script to page."""
    await stealth.apply_stealth_async(page)
    await page.add_init_script("""
        Object.defineProperty(navigator, 'webdriver', {
            get: () => false,
        });
        window.chrome = {
            runtime: {},
            loadTimes: function() {},
            csi: function() {},
            app: {}
        };
    """)
    return page



async def check_login_status(page, context=None) -> bool:
    """Check if the current session on page/context is logged into X."""
    try:
        if context:
            cookies = await context.cookies()
            auth_cookie = any(c.get("name") == "auth_token" for c in cookies)
            if auth_cookie:
                return True

        avatar = await page.query_selector("[data-testid=\"SideNav_AccountSwitcher_Button\"]")
        if avatar:
            return True

        # Try navigating to home if not checked
        if "login" in page.url or "flow" in page.url:
            return False

        cookies = await page.context.cookies()
        return any(c.get("name") == "auth_token" for c in cookies)
    except Exception as e:
        print(f"Login check encountered error: {e}")
        return False


async def cmd_set_auth(auth_token: str):
    """Directly save an existing auth_token cookie into .browser_data."""
    from playwright.async_api import async_playwright

    token_clean = auth_token.strip().strip("'\"")
    print(f"Configuring session with auth_token: {token_clean[:6]}...{token_clean[-4:]}")

    async with async_playwright() as p:
        context = await get_browser_context(p, headless=True)
        await context.add_cookies([
            {
                "name": "auth_token",
                "value": token_clean,
                "domain": ".x.com",
                "path": "/",
                "httpOnly": True,
                "secure": True,
                "sameSite": "None",
            }
        ])
        page = context.pages[0] if context.pages else await context.new_page()
        await prepare_page(page)
        print("Testing authentication on https://x.com/home...")
        logged_in = await check_login_status(page, context)
        await context.close()

    if logged_in:
        print("✅ Session successfully verified and saved!")
    else:
        print("⚠️ Cookie was saved, but verification did not confirm login. Please verify the token.")


async def cmd_login(headless: bool = False):
    """Interactive login helper to store cookies in .browser_data."""
    from playwright.async_api import async_playwright

    print("Launching Chromium browser for X (Twitter) login with anti-detection stealth...")
    print("A browser window will open on your desktop. Please sign in to your X account.")

    async with async_playwright() as p:
        context = await get_browser_context(p, headless=False)
        page = context.pages[0] if context.pages else await context.new_page()
        await prepare_page(page)
        await page.goto("https://x.com/login", timeout=30000)

        print("\nWaiting for you to complete sign-in in the browser window...")
        print("Listening for authenticated session (auth_token cookie)...\n")

        # Poll every 2 seconds for up to 8 minutes
        for i in range(240):
            await page.wait_for_timeout(2000)
            cookies = await context.cookies()
            has_auth = any(c.get("name") == "auth_token" for c in cookies)
            if has_auth:
                print("✅ Successfully authenticated! Your session has been saved to .browser_data.")
                print("You can now run scan and batch export commands.")
                await page.wait_for_timeout(2000)
                break
        else:
            print("⚠️ Timeout waiting for login. Run again when ready.")

        await context.close()




async def cmd_status():
    """Verify session and report local article counts."""
    from playwright.async_api import async_playwright

    print("Checking X login session...")
    async with async_playwright() as p:
        context = await get_browser_context(p, headless=True)
        page = context.pages[0] if context.pages else await context.new_page()
        await prepare_page(page)
        logged_in = await check_login_status(page, context)
        await context.close()


    print(f"X Login Session: {'✅ Active (Logged In)' if logged_in else '❌ Not Logged In (Run login command)'}")

    # Inspect manifest & content
    if MANIFEST_FILE.exists():
        with open(MANIFEST_FILE, "r", encoding="utf-8") as f:
            manifest = json.load(f)
        total = len(manifest)
        exported = sum(1 for m in manifest if m.get("status") == "exported")
        pending = total - exported
        print(f"Discovered in manifest: {total} articles ({exported} exported, {pending} pending)")
    else:
        print("Manifest: No articles scanned yet (Run scan command)")

    exported_files = list(CONTENT_DIR.glob("*.md"))
    print(f"Markdown articles on disk: {len(exported_files)} in {CONTENT_DIR}")


async def cmd_scan(handle: str, max_scrolls: int = 15, headless: bool = False):
    """Scan X profile (/articles or posts) and generate manifest.json."""
    from playwright.async_api import async_playwright

    CONTENT_DIR.mkdir(parents=True, exist_ok=True)
    print(f"Scanning articles for @{handle}...")

    # Load existing manifest if any
    existing_items = {}
    if MANIFEST_FILE.exists():
        try:
            with open(MANIFEST_FILE, "r", encoding="utf-8") as f:
                for item in json.load(f):
                    existing_items[item["url"]] = item
        except Exception:
            pass

    discovered = dict(existing_items)

    async with async_playwright() as p:
        context = await get_browser_context(p, headless=headless)
        page = context.pages[0] if context.pages else await context.new_page()
        await prepare_page(page)

        # Target URLs for articles:

        # 1. Dedicated creator articles studio: https://x.com/i/articles
        # 2. Public profile articles tab: https://x.com/{handle}/articles
        target_urls = [
            "https://x.com/i/articles",
            f"https://x.com/{handle}/articles",
        ]

        for target_url in target_urls:
            print(f"\nNavigating to {target_url}...")
            try:
                await page.goto(target_url, wait_until="domcontentloaded", timeout=25000)
                await page.wait_for_timeout(3500)
            except Exception as e:
                print(f"  Note: Could not reach {target_url}: {e}")
                continue

            # Check if redirected to login
            if "login" in page.url or "flow" in page.url:
                print(f"  ⚠️ Encountered login redirect at {page.url}.")
                continue

            print(f"Scanning {page.url} for article links (up to {max_scrolls} scrolls)...")

            for scroll_idx in range(max_scrolls):
                # Discover articles
                cards = await page.eval_on_selector_all(
                    "article, [data-testid=\"tweet\"], [role=\"article\"], a[href*=\"/article/\"]",
                    """elements => elements.map(el => {
                        let link = el.tagName === 'A' ? el : el.querySelector('a[href*="/article/"], a[href*="/status/"]');
                        const timeEl = el.querySelector ? el.querySelector('time') : null;
                        const headingEl = el.querySelector ? el.querySelector('h1, h2, [role="heading"], [data-testid="article-title"]') : null;
                        const textEl = el.querySelector ? el.querySelector('[data-testid="tweetText"], p') : null;
                        return {
                            url: link ? link.href : (el.href || null),
                            date: timeEl ? (timeEl.getAttribute('datetime') || timeEl.innerText) : null,
                            title: headingEl ? headingEl.innerText.trim() : null,
                            snippet: textEl ? textEl.innerText.trim().slice(0, 150) : null
                        };
                    })"""
                )

                new_count = 0
                for card in cards:
                    url = card.get("url")
                    if not url:
                        continue
                    clean_url = url.split("?")[0]
                    # Only collect actual articles or statuses
                    if "/article/" not in clean_url and "/status/" not in clean_url:
                        continue
                    if clean_url in discovered:
                        continue

                    discovered[clean_url] = {
                        "url": clean_url,
                        "date": card.get("date"),
                        "title": card.get("title") or (card.get("snippet", "")[:60] if card.get("snippet") else "Untitled"),
                        "snippet": card.get("snippet") or "",
                        "scanned_at": datetime.utcnow().isoformat() + "Z",
                        "status": "pending"
                    }
                    new_count += 1

                if new_count > 0:
                    print(f"  Pass {scroll_idx + 1}: +{new_count} entries (Total unique: {len(discovered)})")

                # Scroll down
                prev_height = await page.evaluate("document.body.scrollHeight")
                await page.evaluate("window.scrollBy(0, window.innerHeight * 1.5)")
                await page.wait_for_timeout(2000)
                curr_height = await page.evaluate("document.body.scrollHeight")
                if curr_height == prev_height and scroll_idx > 3:
                    # reached bottom
                    break


        # Also scan highlight tab if articles tab is empty or few
        if len(discovered) == 0:
            print(f"Articles tab returned 0 results. Checking main profile posts...")
            await page.goto(f"https://x.com/{handle}", wait_until="networkidle", timeout=30000)
            await page.wait_for_timeout(3000)
            for scroll_idx in range(min(max_scrolls, 5)):
                cards = await page.eval_on_selector_all(
                    "article, [data-testid=\"tweet\"]",
                    """elements => elements.map(el => {
                        const link = el.querySelector('a[href*="/status/"], a[href*="/article/"]');
                        const timeEl = el.querySelector('time');
                        const textEl = el.querySelector('[data-testid="tweetText"]');
                        return {
                            url: link ? link.href : null,
                            date: timeEl ? timeEl.getAttribute('datetime') : null,
                            snippet: textEl ? textEl.innerText.trim() : null
                        };
                    })"""
                )
                for card in cards:
                    url = card.get("url")
                    if not url:
                        continue
                    clean_url = url.split("?")[0]
                    if clean_url in discovered:
                        continue
                    discovered[clean_url] = {
                        "url": clean_url,
                        "date": card.get("date"),
                        "title": card.get("snippet", "")[:60] if card.get("snippet") else "Post",
                        "snippet": card.get("snippet") or "",
                        "scanned_at": datetime.utcnow().isoformat() + "Z",
                        "status": "pending"
                    }
                await page.evaluate("window.scrollBy(0, window.innerHeight * 1.5)")
                await page.wait_for_timeout(2000)

        await context.close()

    # Save manifest
    manifest_list = list(discovered.values())
    manifest_list.sort(key=lambda x: x.get("date") or "", reverse=True)
    with open(MANIFEST_FILE, "w", encoding="utf-8") as f:
        json.dump(manifest_list, f, indent=2)

    print(f"\n✅ Scan complete! Manifest saved to {MANIFEST_FILE}")
    print(f"Total articles/posts discovered: {len(manifest_list)}")


from dateutil import parser as date_parser

def parse_x_date(raw_date_str: str) -> str:
    """Parse various X timestamp formats into ISO 8601 string."""
    if not raw_date_str:
        return datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    raw_clean = raw_date_str.replace("·", " ").strip()
    try:
        dt = date_parser.parse(raw_clean)
        return dt.strftime("%Y-%m-%dT%H:%M:%SZ")
    except Exception:
        return datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")


def clean_x_title(raw_title: str, text_content: str) -> str:
    """Extract a concise, human-readable title without platform chrome."""
    if raw_title:
        # Strip common prefixes like 'Name on X: "..."'
        cleaned = re.sub(r"^.*? on X:\s*[\"']?", "", raw_title)
        cleaned = re.sub(r"[\"']\s*$", "", cleaned)
        if len(cleaned.strip()) > 5 and not cleaned.lower().startswith("don't miss"):
            # Truncate at first newline or 90 chars
            first_line = cleaned.split("\n")[0].strip()
            return first_line[:90]

    # Fallback to first line of text
    lines = [line.strip() for line in text_content.split("\n") if line.strip()]
    if lines:
        first = lines[0]
        # Remove URLs
        first = re.sub(r"https?://\S+", "", first).strip()
        if len(first) > 5:
            return first[:90]

    return "Untitled Post"


async def extract_article_content(page, url: str) -> dict:
    """Visit an article or post URL and extract title, metadata, and clean body Markdown."""
    await page.goto(url, wait_until="domcontentloaded", timeout=30000)
    await page.wait_for_timeout(4000)

    # Click any "Show more" / "Read more" expanders
    try:
        show_more_buttons = await page.query_selector_all("text='Show more', text='Read more'")
        for btn in show_more_buttons:
            if await btn.is_visible():
                await btn.click()
                await page.wait_for_timeout(500)
    except Exception:
        pass

    # Extract time from page if present
    date_val = None
    time_el = await page.query_selector("time")
    if time_el:
        attr_dt = await time_el.get_attribute("datetime")
        text_dt = await time_el.inner_text()
        date_val = parse_x_date(attr_dt or text_dt)

    # Prioritize <article> container for full articles
    body_html = None
    articles = await page.query_selector_all("article")
    if articles:
        body_html = await articles[0].inner_html()
    else:
        for selector in [
            "[data-testid=\"article-body\"]",
            "[data-testid=\"tweetText\"]",
            "main"
        ]:
            container = await page.query_selector(selector)
            if container:
                html = await container.inner_html()
                if len(html) > 50:
                    body_html = html
                    break

    if not body_html:
        body_html = await page.content()

    soup = BeautifulSoup(body_html, "html.parser")

    # Clean UI buttons, actions, navigations, svg
    for tag in soup(["script", "style", "nav", "button", "svg", "form"]):
        tag.decompose()

    # Expand t.co links to real destinations if title attribute is present
    for a in soup.find_all("a", href=True):
        title_attr = a.get("title")
        if title_attr and title_attr.startswith("http"):
            a["href"] = title_attr

    # Convert to Markdown
    md_content = markdownify.markdownify(
        str(soup),
        heading_style="ATX",
        bullets="-",
        strip=["button", "script", "style"]
    ).strip()

    # Extract date from footer if not found yet (e.g. "[1:59 PM · Nov 8, 2026]")
    if not date_val or date_val.startswith(datetime.utcnow().strftime("%Y-%m-%d")):
        date_match = re.search(r"\[(\d{1,2}:\d{2}\s*(?:AM|PM)\s*·\s*[A-Za-z]+\s+\d{1,2},\s*\d{4})\]", md_content)
        if date_match:
            raw_matched = date_match.group(1).replace("·", " ").strip()
            try:
                date_val = date_parser.parse(raw_matched).strftime("%Y-%m-%dT%H:%M:%SZ")
            except Exception:
                pass

    if not date_val:
        date_val = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

    # Extract read time if present (e.g. "31 min read")
    read_time = None
    read_time_match = re.search(r"(\d+\s*min\s*read)", md_content, re.IGNORECASE)
    if read_time_match:
        read_time = read_time_match.group(1)

    # Extract cover image if present
    cover_image = None
    cover_match = re.search(r"!\[(?:Article cover image|Cover image|[^\]]*)\]\((https://pbs\.twimg\.com/media/[^\)\s]+)\)", md_content)
    if cover_match:
        cover_image = cover_match.group(1)

    # Extract title: look for "# Title" in markdown
    title = None
    h1_match = re.search(r"^#\s+(.+)$", md_content, re.MULTILINE)
    if h1_match:
        title = h1_match.group(1).strip()
    else:
        # Check page title
        raw_page_title = await page.title()
        title = clean_x_title(raw_page_title, md_content)

    # Strip author profile header at top
    md_content = re.sub(
        r"^\[!\[@[^\]]+\]\([^\)]+\)\]\(/[^\)]+\)\s*\n\s*\[[^\]]+\]\(/[^\)]+\)\[@[^\]]+\]\(/[^\)]+\)\s*",
        "",
        md_content.strip()
    )

    # Strip author footer card and metrics at bottom
    md_content = re.split(
        r"\[!\[@[^\]]+\]\([^\)]+\)\]\(/[^\)]+\)\s*\n\s*\[Richard Collins",
        md_content
    )[0]
    md_content = re.sub(r"\[Last edited [^\]]+\]\([^\)]+\)·\[[\d,]+\s*Views\]\([^\)]+\)", "", md_content)
    md_content = re.sub(r"\[[\d,]+\s*Views\]\([^\)]+\)", "", md_content)
    md_content = re.sub(r"\[\d+\]\(/compose/post\?[^\)]+\)", "", md_content)
    md_content = re.sub(r"\n{3,}", "\n\n", md_content).strip()

    return {
        "title": title or "Untitled Article",
        "date": date_val,
        "read_time": read_time,
        "cover_image": cover_image,
        "url": url,
        "content": md_content,
    }




async def cmd_export(
    batch_size: int = 5,
    limit: int = None,
    direct_url: str = None,
    urls_file: str = None,
    headless: bool = False
):
    """Export scanned articles from manifest or URL list into Markdown files."""
    from playwright.async_api import async_playwright

    CONTENT_DIR.mkdir(parents=True, exist_ok=True)

    items_to_export = []
    manifest = []

    if direct_url:
        items_to_export = [{
            "url": direct_url,
            "title": "Direct Article",
            "date": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
            "status": "pending"
        }]
    elif urls_file:
        file_path = Path(urls_file)
        if not file_path.exists():
            print(f"❌ URLs file not found: {urls_file}")
            return
        with open(file_path, "r", encoding="utf-8") as f:
            raw_lines = [line.strip() for line in f if line.strip() and not line.startswith("#")]
        items_to_export = [{
            "url": url,
            "title": "Queued Article",
            "date": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
            "status": "pending"
        } for url in raw_lines]
        print(f"Loaded {len(items_to_export)} URLs from {urls_file}")
    else:
        if not MANIFEST_FILE.exists():
            print(f"❌ Manifest not found at {MANIFEST_FILE}. Run scan first or pass --url / --urls-file.")
            return

        with open(MANIFEST_FILE, "r", encoding="utf-8") as f:
            manifest = json.load(f)

        items_to_export = [m for m in manifest if m.get("status") != "exported"]


    if not items_to_export:
        print("✅ All articles in manifest are already exported! Nothing to do.")
        return

    if limit:
        items_to_export = items_to_export[:limit]

    print(f"Starting export for {len(items_to_export)} articles (batch size: {batch_size})...")

    async with async_playwright() as p:
        context = await get_browser_context(p, headless=headless)
        page = context.pages[0] if context.pages else await context.new_page()
        await prepare_page(page)

        processed_in_batch = 0


        for i, item in enumerate(items_to_export, 1):
            url = item["url"]
            print(f"\n[{i}/{len(items_to_export)}] Processing: {url}")

            try:
                data = await extract_article_content(page, url)
                title = data["title"]
                date_str = data["date"]
                content = data["content"]

                # Generate clean filename: YYYY-MM-DD-slug.md
                date_prefix = date_str[:10] if date_str else datetime.utcnow().strftime("%Y-%m-%d")
                clean_slug = slugify(title)
                filename = f"{date_prefix}-{clean_slug}.md"
                out_path = CONTENT_DIR / filename

                # Frontmatter
                frontmatter = {
                    "title": title,
                    "date": date_str,
                    "author": "Richard Collins",
                    "handle": f"@{DEFAULT_HANDLE}",
                    "original_url": url,
                    "platform": "x",
                    "source": "x-article",
                    "tags": ["writing", "research", "ai-collaboration"],
                }
                if data.get("read_time"):
                    frontmatter["read_time"] = data["read_time"]
                if data.get("cover_image"):
                    frontmatter["cover_image"] = data["cover_image"]

                file_text = "---\n"
                file_text += yaml.dump(frontmatter, sort_keys=False, allow_unicode=True)
                file_text += "---\n\n"
                file_text += f"*Originally published on [X]({url}) on {date_prefix}*\n\n"
                file_text += "---\n\n"
                file_text += content + "\n"


                with open(out_path, "w", encoding="utf-8") as f:
                    f.write(file_text)

                print(f"  -> Saved to {out_path.name} ({len(content)} chars)")

                # Update manifest status
                item["status"] = "exported"
                item["exported_at"] = datetime.utcnow().isoformat() + "Z"
                item["file"] = str(out_path.relative_to(ROOT_DIR))

                # Save manifest progress after each file
                if manifest:
                    for m in manifest:
                        if m["url"] == url:
                            m.update(item)
                    with open(MANIFEST_FILE, "w", encoding="utf-8") as f:
                        json.dump(manifest, f, indent=2)

                processed_in_batch += 1

                # Batch pause to respect rate limits
                if processed_in_batch % batch_size == 0 and i < len(items_to_export):
                    print(f"  Pausing 5 seconds between batches...")
                    await asyncio.sleep(5)
                else:
                    await asyncio.sleep(2)

            except Exception as e:
                print(f"  ❌ Error exporting {url}: {e}")
                item["status"] = "error"
                item["error"] = str(e)

        await context.close()

    print(f"\n🎉 Batch export finished! Check {CONTENT_DIR} for exported Markdown files.")


def main():
    parser = argparse.ArgumentParser(description="X (Twitter) Article Scraper & Markdown Converter")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # login command
    subparsers.add_parser("login", help="Open browser to log into X and save cookies")

    # set-auth command
    set_auth_p = subparsers.add_parser("set-auth", help="Directly set auth_token cookie value")
    set_auth_p.add_argument("token", help="Value of auth_token cookie from existing browser")

    # status command
    subparsers.add_parser("status", help="Check current login session and article stats")


    # scan command
    scan_p = subparsers.add_parser("scan", help="Scan X profile to find article URLs")
    scan_p.add_argument("--handle", default=DEFAULT_HANDLE, help="X username handle (default: %(default)s)")
    scan_p.add_argument("--max-scrolls", type=int, default=15, help="Number of scroll passes (default: 15)")
    scan_p.add_argument("--headless", action="store_true", help="Run browser in headless mode")

    # export command
    exp_p = subparsers.add_parser("export", help="Export articles from manifest to Markdown")
    exp_p.add_argument("--batch-size", type=int, default=5, help="Articles to process per batch (default: 5)")
    exp_p.add_argument("--limit", type=int, default=None, help="Maximum articles to process")
    exp_p.add_argument("--url", default=None, help="Single article URL to export directly")
    exp_p.add_argument("--urls-file", default=None, help="File containing list of URLs to export")
    exp_p.add_argument("--headless", action="store_true", help="Run browser in headless mode")

    args = parser.parse_args()

    if args.command == "login":
        asyncio.run(cmd_login())
    elif args.command == "set-auth":
        asyncio.run(cmd_set_auth(args.token))
    elif args.command == "status":
        asyncio.run(cmd_status())

    elif args.command == "scan":
        asyncio.run(cmd_scan(handle=args.handle, max_scrolls=args.max_scrolls, headless=args.headless))
    elif args.command == "export":
        asyncio.run(cmd_export(
            batch_size=args.batch_size,
            limit=args.limit,
            direct_url=args.url,
            urls_file=args.urls_file,
            headless=args.headless
        ))


if __name__ == "__main__":
    main()

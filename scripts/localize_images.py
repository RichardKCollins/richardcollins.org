#!/usr/bin/env python3
"""
Download all remote Twitter/X media images referenced in markdown files
to local assets/images/articles/ and rewrite links to local paths.
"""

import os
import re
from pathlib import Path
from urllib.parse import parse_qs, urlparse
import requests

ROOT_DIR = Path(__file__).resolve().parent.parent
CONTENT_DIR = ROOT_DIR / "content" / "x-articles"
ASSETS_IMG_DIR = ROOT_DIR / "assets" / "images" / "articles"

USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"


def get_image_filename(url: str, content_type: str = None) -> str:
    """Generate local filename from Twitter media URL."""
    parsed = urlparse(url)
    base_name = os.path.basename(parsed.path)
    # If base_name has extension like HWoI0I7XYAA-UN9.jpg
    if "." in base_name:
        return base_name

    # Check query params for format
    qs = parse_qs(parsed.query)
    fmt = qs.get("format", ["jpg"])[0]

    if content_type:
        if "png" in content_type:
            fmt = "png"
        elif "webp" in content_type:
            fmt = "webp"
        elif "jpeg" in content_type or "jpg" in content_type:
            fmt = "jpg"

    return f"{base_name}.{fmt}"


def main():
    ASSETS_IMG_DIR.mkdir(parents=True, exist_ok=True)
    md_files = list(CONTENT_DIR.glob("*.md"))
    print(f"Scanning {len(md_files)} Markdown files for remote Twitter images...")

    # Regex matching pbs.twimg.com URLs
    img_pattern = re.compile(r"https://pbs\.twimg\.com/(?:media|profile_images)/[^\)\"\s]+")

    url_to_local = {}

    # Collect all unique image URLs
    for md_path in md_files:
        with open(md_path, "r", encoding="utf-8") as f:
            content = f.read()
        for match in img_pattern.findall(content):
            # Clean trailing brackets or markdown artifacts if any
            clean_url = match.rstrip(")]\"'")
            if clean_url not in url_to_local:
                url_to_local[clean_url] = None

    print(f"Found {len(url_to_local)} unique remote images to localize.")

    session = requests.Session()
    session.headers.update({"User-Agent": USER_AGENT})

    downloaded = 0
    skipped = 0

    for i, (remote_url, _) in enumerate(url_to_local.items(), 1):
        # Determine best download URL (request large/orig if possible)
        parsed = urlparse(remote_url)
        base = remote_url.split("?")[0]
        qs = parse_qs(parsed.query)

        fmt = qs.get("format", [None])[0]
        if not fmt:
            if base.endswith(".png"):
                fmt = "png"
            elif base.endswith(".jpg") or base.endswith(".jpeg"):
                fmt = "jpg"
            else:
                fmt = "jpg"

        # Request high quality
        fetch_url = f"{base}?format={fmt}&name=large" if "?" not in base else remote_url

        try:
            # Check existing file
            candidate_name = get_image_filename(remote_url)
            local_file = ASSETS_IMG_DIR / candidate_name

            if local_file.exists() and local_file.stat().st_size > 500:
                url_to_local[remote_url] = f"/assets/images/articles/{local_file.name}"
                skipped += 1
                continue

            print(f"[{i}/{len(url_to_local)}] Downloading {base} ...")
            resp = session.get(fetch_url, timeout=20)
            if resp.status_code != 200:
                # Try original url
                resp = session.get(remote_url, timeout=20)

            if resp.status_code == 200:
                final_name = get_image_filename(remote_url, resp.headers.get("Content-Type"))
                target_path = ASSETS_IMG_DIR / final_name
                with open(target_path, "wb") as f:
                    f.write(resp.content)
                url_to_local[remote_url] = f"/assets/images/articles/{final_name}"
                downloaded += 1
                print(f"  -> Saved {final_name} ({len(resp.content) / 1024:.1f} KB)")
            else:
                print(f"  ❌ Failed (HTTP {resp.status_code}): {remote_url}")

        except Exception as e:
            print(f"  ❌ Error downloading {remote_url}: {e}")

    print(f"\nDownloaded: {downloaded}, Cached/Skipped: {skipped}")

    # Now rewrite Markdown files
    print("\nRewriting Markdown files with local image references...")
    updated_files = 0

    for md_path in md_files:
        with open(md_path, "r", encoding="utf-8") as f:
            content = f.read()

        new_content = content
        replaced_in_file = 0

        for remote_url, local_path in url_to_local.items():
            if local_path and remote_url in new_content:
                new_content = new_content.replace(remote_url, local_path)
                replaced_in_file += 1

        if replaced_in_file > 0:
            with open(md_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            updated_files += 1
            print(f"  Updated {md_path.name} ({replaced_in_file} images rewritten)")

    print(f"\n✅ All images localized and {updated_files} Markdown files updated!")


if __name__ == "__main__":
    main()

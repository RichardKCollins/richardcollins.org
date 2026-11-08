#!/usr/bin/env python3
"""
Static Site Generator for richardcollins.org.
Reads Markdown files from content/x-articles/ (and other content folders),
renders them into styled HTML pages, generates the /articles archive,
and updates index.html.
"""

import html
import json
import os
import re
from datetime import datetime
from pathlib import Path

import markdown
import yaml

ROOT_DIR = Path(__file__).resolve().parent.parent
CONTENT_DIR = ROOT_DIR / "content" / "x-articles"
ARTICLES_OUT_DIR = ROOT_DIR / "articles"
INDEX_FILE = ROOT_DIR / "index.html"


def parse_markdown_file(path: Path) -> dict:
    """Parse a Markdown file with YAML frontmatter."""
    with open(path, "r", encoding="utf-8") as f:
        raw = f.read()

    frontmatter = {}
    body = raw

    if raw.startswith("---"):
        parts = raw.split("---", 2)
        if len(parts) >= 3:
            try:
                frontmatter = yaml.safe_load(parts[1]) or {}
                body = parts[2].strip()
            except Exception as e:
                print(f"Error parsing YAML in {path.name}: {e}")

    # Generate slug from filename
    slug = path.stem
    # If slug has YYYY-MM-DD- prefix, keep clean slug
    slug_clean = re.sub(r"^\d{4}-\d{2}-\d{2}-", "", slug)

    return {
        "file_name": path.name,
        "slug": slug_clean,
        "full_slug": slug,
        "title": frontmatter.get("title", slug_clean.replace("-", " ").title()),
        "date": frontmatter.get("date", ""),
        "author": frontmatter.get("author", "Richard Collins"),
        "handle": frontmatter.get("handle", "@RichardKCollin2"),
        "original_url": frontmatter.get("original_url", ""),
        "read_time": frontmatter.get("read_time", ""),
        "cover_image": frontmatter.get("cover_image", ""),
        "tags": frontmatter.get("tags", ["writing", "research"]),
        "markdown_body": body,
    }


def format_date_display(iso_date: str) -> str:
    """Convert ISO date to readable string like 'Nov 8, 2026'."""
    if not iso_date:
        return ""
    try:
        clean = iso_date.replace("Z", "+00:00")
        dt = datetime.fromisoformat(clean)
        return dt.strftime("%b %d, %Y")
    except Exception:
        return iso_date[:10]


def render_article_html(article: dict, prev_art: dict = None, next_art: dict = None) -> str:
    """Render a full HTML document for a single article."""
    # Convert body to HTML
    md_extensions = ["fenced_code", "tables", "toc", "sane_lists", "attr_list"]
    html_body = markdown.markdown(article["markdown_body"], extensions=md_extensions)

    display_date = format_date_display(article["date"])
    title_escaped = html.escape(article["title"])
    read_time = article.get("read_time") or ""

    cover_img_html = ""
    if article.get("cover_image"):
        cover_img_html = f'''
        <div class="article-cover-wrapper">
          <img src="{article['cover_image']}" alt="{title_escaped}" class="article-cover-img">
        </div>'''

    orig_link_html = ""
    if article.get("original_url"):
        orig_link_html = f'''
        <a href="{article['original_url']}" class="original-link" target="_blank" rel="noopener">
          Originally published on X ↗
        </a>'''

    prev_link = f'<a href="/articles/{prev_art["slug"]}/" class="btn-link">← {html.escape(prev_art["title"][:40])}...</a>' if prev_art else '<span></span>'
    next_link = f'<a href="/articles/{next_art["slug"]}/" class="btn-link">{html.escape(next_art["title"][:40])}... →</a>' if next_art else '<span></span>'

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title_escaped} - Richard Collins</title>
  <meta name="description" content="{title_escaped}">
  <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220%22%20width=%22100%22%20height=%22100%22><text y=%22.9em%22 font-size=%2290%22>🌐</text></svg>">
  <link rel="stylesheet" href="/style.css">
  <meta property="og:title" content="{title_escaped}">
  <meta property="og:type" content="article">
  {f'<meta property="og:image" content="{article["cover_image"]}">' if article.get("cover_image") else ''}
</head>
<body>

  <header class="site-header">
    <div class="container nav-container">
      <a href="/" class="brand">Richard Collins</a>
      <nav>
        <ul class="nav-links">
          <li><a href="/#about">About</a></li>
          <li><a href="/#projects">Projects</a></li>
          <li><a href="/articles/" class="active">Articles</a></li>
          <li><a href="/#contact">Contact</a></li>
        </ul>
      </nav>
    </div>
  </header>

  <main class="container article-page">
    <nav class="breadcrumb-nav">
      <a href="/articles/" class="breadcrumb-link">← All Articles</a>
    </nav>

    <article class="article-detail">
      <header class="article-header">
        <div class="article-meta-top">
          <time datetime="{article['date']}">{display_date}</time>
          {f'<span class="meta-dot">·</span><span class="read-time">{read_time}</span>' if read_time else ''}
          {f'<span class="meta-dot">·</span>{orig_link_html}' if orig_link_html else ''}
        </div>
        <h1 class="article-title">{title_escaped}</h1>
        <div class="article-author">
          <span>By <strong>{article['author']}</strong> ({article['handle']})</span>
        </div>
      </header>

      {cover_img_html}

      <div class="article-content">
        {html_body}
      </div>

      <footer class="article-footer-nav">
        <div class="article-nav-links">
          {prev_link}
          {next_link}
        </div>
        <div class="article-footer-author">
          <p><strong>Richard Collins</strong> is exploring open distributed systems, physical modeling, and global knowledge networks.</p>
          <p><a href="/articles/">Explore more publications</a> or connect on <a href="https://x.com/RichardKCollin2" target="_blank" rel="noopener">X (@RichardKCollin2)</a>.</p>
        </div>
      </footer>
    </article>
  </main>

  <footer class="site-footer">
    <div class="container footer-content">
      <p>&copy; {datetime.utcnow().year} Richard Collins &middot; <a href="/">richardcollins.org</a></p>
    </div>
  </footer>

</body>
</html>
'''


def render_archive_html(articles: list) -> str:
    """Render the /articles/ index page."""
    cards_html = []
    for art in articles:
        date_str = format_date_display(art["date"])
        title = html.escape(art["title"])
        read_time = art.get("read_time", "")
        slug = art["slug"]

        thumb_html = ""
        if art.get("cover_image"):
            thumb_html = f'''
            <div class="archive-thumb">
              <img src="{art['cover_image']}" alt="{title}" loading="lazy">
            </div>'''

        cards_html.append(f'''
        <a href="/articles/{slug}/" class="archive-card">
          {thumb_html}
          <div class="archive-card-body">
            <div class="card-meta">
              <time datetime="{art['date']}">{date_str}</time>
              {f'<span>·</span><span>{read_time}</span>' if read_time else ''}
            </div>
            <h3>{title}</h3>
            <span class="read-more">Read Article →</span>
          </div>
        </a>''')

    cards_joined = "\n".join(cards_html)

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Articles & Writing - Richard Collins</title>
  <meta name="description" content="Long-form articles, system architecture research, and AI collaborations by Richard Collins.">
  <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220%22%20width=%22100%22%20height=%22100%22><text y=%22.9em%22 font-size=%2290%22>🌐</text></svg>">
  <link rel="stylesheet" href="/style.css">
</head>
<body>

  <header class="site-header">
    <div class="container nav-container">
      <a href="/" class="brand">Richard Collins</a>
      <nav>
        <ul class="nav-links">
          <li><a href="/#about">About</a></li>
          <li><a href="/#projects">Projects</a></li>
          <li><a href="/articles/" class="active">Articles</a></li>
          <li><a href="/#contact">Contact</a></li>
        </ul>
      </nav>
    </div>
  </header>

  <main class="container archive-page">
    <section class="archive-hero">
      <span class="hero-tag">Publications</span>
      <h1>Articles & Essays</h1>
      <p class="hero-lead">
        Investigations into internet architecture, knowledge networks, physical modeling, and human-AI collaborative workflows.
      </p>
      <div class="search-bar-wrapper">
        <input type="text" id="article-search" placeholder="Search {len(articles)} articles by title or keyword..." autocomplete="off">
      </div>
    </section>

    <section class="archive-grid" id="articles-list">
      {cards_joined}
    </section>
  </main>

  <footer class="site-footer">
    <div class="container footer-content">
      <p>&copy; {datetime.utcnow().year} Richard Collins &middot; <a href="/">richardcollins.org</a></p>
    </div>
  </footer>

  <script>
    const searchInput = document.getElementById('article-search');
    const articlesList = document.getElementById('articles-list');
    const cards = Array.from(articlesList.getElementsByClassName('archive-card'));

    searchInput.addEventListener('input', (e) => {{
      const query = e.target.value.toLowerCase().trim();
      cards.forEach(card => {{
        const text = card.innerText.toLowerCase();
        if (text.includes(query)) {{
          card.style.display = '';
        }} else {{
          card.style.display = 'none';
        }}
      }});
    }});
  </script>

</body>
</html>
'''


def update_homepage(articles: list):
    """Update index.html with the latest articles."""
    if not INDEX_FILE.exists():
        return

    with open(INDEX_FILE, "r", encoding="utf-8") as f:
        html_content = f.read()

    # Update Navigation if Articles is missing
    if '<li><a href="/articles/">Articles</a></li>' not in html_content:
        html_content = html_content.replace(
            '<li><a href="#projects">Projects</a></li>',
            '<li><a href="#projects">Projects</a></li>\n          <li><a href="/articles/">Articles</a></li>'
        )

    # Build top 6 recent articles HTML
    recent = articles[:6]
    items_html = []
    for art in recent:
        title = html.escape(art["title"])
        date_str = format_date_display(art["date"])
        read_time = art.get("read_time", "")
        slug = art["slug"]
        meta_str = f"{date_str} · {read_time}" if read_time else date_str

        items_html.append(f'''        <div class="item-row">
          <a href="/articles/{slug}/" class="item-title" style="text-decoration: none; color: inherit;">{title} <span class="arrow">→</span></a>
          <span class="item-meta">{meta_str}</span>
        </div>''')

    items_block = "\n".join(items_html)

    # Replace the items-list inside #notes section
    new_section = f'''    <!-- Writing / Notes -->
    <section class="section" id="notes">
      <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 1.5rem;">
        <h2 class="section-title" style="margin-bottom: 0;">Writing & Publications</h2>
        <a href="/articles/" class="btn-link" style="font-size: 0.9rem;">View All {len(articles)} Articles →</a>
      </div>
      <div class="item-list">
{items_block}
      </div>
    </section>'''

    pattern = re.compile(r'<!-- Writing / Notes -->.*?<\/section>', re.DOTALL)
    if pattern.search(html_content):
        updated_html = pattern.sub(new_section, html_content)
        with open(INDEX_FILE, "w", encoding="utf-8") as f:
            f.write(updated_html)
        print("  Updated index.html Writing section with latest articles.")


def main():
    print("Building static site for richardcollins.org...")

    md_files = sorted(list(CONTENT_DIR.glob("*.md")), reverse=True)
    articles = [parse_markdown_file(p) for p in md_files]
    # Sort by date descending
    articles.sort(key=lambda a: a.get("date") or "", reverse=True)

    print(f"Loaded {len(articles)} articles.")

    # Generate individual article HTML pages
    for i, art in enumerate(articles):
        out_dir = ARTICLES_OUT_DIR / art["slug"]
        out_dir.mkdir(parents=True, exist_ok=True)
        out_file = out_dir / "index.html"

        prev_art = articles[i + 1] if i + 1 < len(articles) else None
        next_art = articles[i - 1] if i > 0 else None

        html_content = render_article_html(art, prev_art, next_art)
        with open(out_file, "w", encoding="utf-8") as f:
            f.write(html_content)

    print(f"  Rendered {len(articles)} article pages under articles/<slug>/index.html")

    # Generate /articles/ archive page
    ARTICLES_OUT_DIR.mkdir(parents=True, exist_ok=True)
    archive_html = render_archive_html(articles)
    with open(ARTICLES_OUT_DIR / "index.html", "w", encoding="utf-8") as f:
        f.write(archive_html)
    print("  Rendered archive index at articles/index.html")

    # Update homepage
    update_homepage(articles)

    print("\n✅ Build complete!")


if __name__ == "__main__":
    main()

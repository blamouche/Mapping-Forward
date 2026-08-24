#!/usr/bin/env python3
"""
Static site generator for Mapping-Forward veille.
Pure Python stdlib — no Node, no pip, no external dependencies.
Reads markdown articles from ../src/, generates HTML pages in dist/.
"""

import os
import re
import html
import glob
import json
import hashlib
from datetime import datetime, date, timedelta
from collections import defaultdict, OrderedDict, Counter
from html import escape

# ─── Paths ───────────────────────────────────────────────────────────────────
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_DIR = os.path.dirname(SCRIPT_DIR)
SRC_DIR = os.path.join(REPO_DIR, "src")
DIST_DIR = os.path.join(SCRIPT_DIR, "dist")
TEMPLATE_DIR = os.path.join(SCRIPT_DIR, "templates")

# ─── Config ───────────────────────────────────────────────────────────────────
SITE_TITLE = "Mapping Forward"
SITE_SUBTITLE = "Cartography and geospatial intelligence watch"
SITE_URL = "https://mappingforward.fr"  # adjust as needed
SITE_DESCRIPTION = "Daily synthesis of articles on cartography, mapping, geospatial data, and geographic intelligence"
SITE_LANG = "en"
SITE_AUTHOR = "Benoit Lamouche"
ARTICLES_PER_PAGE = 25

def plural(n, word):
    """English pluralization helper: plural(1, 'article') -> '1 article'."""
    return f"{n} {word}" if n == 1 else f"{n} {word}s"

# ─── Markdown parsing ─────────────────────────────────────────────────────────

def parse_article(filepath):
    """Parse a markdown article file into a dict."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    data = {
        "filepath": filepath,
        "filename": os.path.basename(filepath),
        "title": "",
        "source": "",
        "date": "",
        "author": "",
        "keywords": "",
        "elevator_pitch": "",
        "takeaways": [],
        "synthesis": "",
        "raw": content,
    }

    # Extract title (first # heading)
    m = re.match(r"^#\s+(.+)$", content, re.MULTILINE)
    if m:
        data["title"] = m.group(1).strip()

    # Extract metadata fields (**Source**: ..., **Date**: ..., etc.)
    for field in ["Source", "Date", "Author", "Keywords"]:
        m = re.search(rf"\*\*{field}\*\*:\s*(.+)$", content, re.MULTILINE)
        if m:
            val = m.group(1).strip()
            key = field.lower()
            if key == "source":
                data["source"] = val
            elif key == "date":
                data["date"] = val
            elif key == "author":
                data["author"] = val
            elif key == "keywords":
                data["keywords"] = val

    # Extract elevator pitch
    m = re.search(r"##\s*Elevator pitch\s*\n(.+?)(?=\n##|\Z)", content, re.DOTALL)
    if m:
        data["elevator_pitch"] = m.group(1).strip()

    # Extract takeaways
    m = re.search(r"##\s*Takeaways\s*\n(.+?)(?=\n##|\Z)", content, re.DOTALL)
    if m:
        takeaway_block = m.group(1).strip()
        data["takeaways"] = [
            line.lstrip("- ").strip()
            for line in takeaway_block.split("\n")
            if line.strip().startswith("-")
        ]

    # Extract synthesis
    m = re.search(r"##\s*Synthesis\s*\n(.+?)(?=\n##|\Z)", content, re.DOTALL)
    if m:
        data["synthesis"] = m.group(1).strip()

    # Extract date from filename if not in metadata: YYYYMMDD-slug.md
    fname = os.path.basename(filepath)
    m = re.match(r"(\d{4})(\d{2})(\d{2})-", fname)
    if m:
        data["date_sort"] = f"{m.group(1)}-{m.group(2)}-{m.group(3)}"
        data["year"] = m.group(1)
        data["month"] = m.group(2)
        data["day"] = m.group(3)
    else:
        data["date_sort"] = data["date"] or "unknown"
        data["year"] = ""
        data["month"] = ""
        data["day"] = ""

    # Generate slug and URL path (relative to site root, no leading slash —
    # keeps the site browsable both via a web server and directly via file://)
    slug = fname.replace(".md", "")
    data["slug"] = slug
    if data["year"] and data["month"]:
        data["url"] = f"articles/{data['year']}-{data['month']}/{slug}.html"
    else:
        data["url"] = f"articles/{slug}.html"

    return data


def load_all_articles():
    """Load all articles from src/ directory, sorted by date descending."""
    articles = []
    for filepath in glob.glob(os.path.join(SRC_DIR, "**", "*.md"), recursive=True):
        try:
            data = parse_article(filepath)
            articles.append(data)
        except Exception as e:
            print(f"WARNING: Failed to parse {filepath}: {e}")
    articles.sort(key=lambda a: a["date_sort"], reverse=True)
    return articles


# ─── HTML helpers ─────────────────────────────────────────────────────────────

def md_to_html(text):
    """Minimal markdown to HTML: paragraphs, bold, italic, links, lists."""
    if not text:
        return ""
    lines = text.split("\n")
    html_lines = []
    in_list = False
    for line in lines:
        stripped = line.strip()
        if not stripped:
            if in_list:
                html_lines.append("</ul>")
                in_list = False
            html_lines.append("")
            continue
        if stripped.startswith("- "):
            if not in_list:
                html_lines.append("<ul>")
                in_list = True
            item = stripped[2:]
            item = inline_md(item)
            html_lines.append(f"<li>{item}</li>")
        else:
            if in_list:
                html_lines.append("</ul>")
                in_list = False
            html_lines.append(f"<p>{inline_md(stripped)}</p>")
    if in_list:
        html_lines.append("</ul>")
    return "\n".join(html_lines)


def inline_md(text):
    """Convert inline markdown (bold, italic, links) to HTML."""
    # Links [text](url)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2" target="_blank" rel="noopener">\1</a>', text)
    # Bold **text**
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    # Italic *text* (but not ** which is bold)
    text = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"<em>\1</em>", text)
    # Escape remaining HTML
    # (we escape after, so links/bold tags survive)
    return text


def page_html(title, body, nav_active="", base=""):
    """Wrap content in full HTML page with CSS.

    `base` is the relative path prefix back to the site root (e.g. "" at the
    root, "../../" from articles/YYYY-MM/*.html). Using relative links
    throughout means the generated site works both served by a web server
    and opened directly via file://.
    """
    nav = f"""
<nav class="navbar">
    <div class="nav-brand">
        <a href="{base}index.html">🗺️ {SITE_TITLE}</a>
    </div>
    <div class="nav-links">
        <a href="{base}index.html" class="{ 'active' if nav_active == 'home' else '' }">Home</a>
        <a href="{base}archives.html" class="{ 'active' if nav_active == 'archives' else '' }">Archives</a>
        <a href="{base}feed.xml" class="{ 'active' if nav_active == 'rss' else '' }">RSS</a>
        <a href="https://mappingforward.substack.com" target="_blank" rel="noopener">Substack</a>
    </div>
</nav>"""
    return f"""<!DOCTYPE html>
<html lang="{SITE_LANG}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{escape(title)} — {SITE_TITLE}</title>
    <meta name="description" content="{escape(SITE_DESCRIPTION)}">
    <link rel="alternate" type="application/rss+xml" title="{SITE_TITLE}" href="{base}feed.xml">
    <link rel="stylesheet" href="{base}style.css">
</head>
<body>
{nav}
<main>
{body}
</main>
<footer class="site-footer">
    <p>{SITE_TITLE} — {SITE_SUBTITLE}</p>
    <p>Static site generated on {datetime.now().strftime("%d %b %Y at %H:%M")} — <a href="https://github.com/blamouche/Mapping-Forward">Source</a></p>
</footer>
</body>
</html>"""


# ─── Page generators ──────────────────────────────────────────────────────────

MONTH_NAMES_EN = {
    1: "January", 2: "February", 3: "March", 4: "April",
    5: "May", 6: "June", 7: "July", 8: "August",
    9: "September", 10: "October", 11: "November", 12: "December"
}
MONTH_ABBR_EN = {
    1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr", 5: "May", 6: "Jun",
    7: "Jul", 8: "Aug", 9: "Sep", 10: "Oct", 11: "Nov", 12: "Dec"
}
DAY_NAMES_EN = {
    0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday",
    4: "Friday", 5: "Saturday", 6: "Sunday"
}


def generate_heatmap(articles):
    """Generate a GitHub-style contribution heatmap (articles per day, last 12 months).

    Pure HTML/CSS grid, no JavaScript — cell tooltips use the native `title`
    attribute, consistent with the rest of the site.
    """
    counts = Counter()
    for a in articles:
        if re.match(r"\d{4}-\d{2}-\d{2}", a["date_sort"]):
            counts[a["date_sort"]] += 1

    today = date.today()
    # Align the grid to full weeks (Sunday -> Saturday) covering the trailing year
    range_start = today - timedelta(days=364)
    range_start -= timedelta(days=(range_start.weekday() + 1) % 7)  # back up to Sunday
    range_end = today + timedelta(days=(5 - today.weekday()) % 7)  # forward to Saturday

    total_days = (range_end - range_start).days + 1
    weeks = total_days // 7

    def level_for(n):
        if n <= 0:
            return 0
        if n <= 2:
            return 1
        if n <= 4:
            return 2
        if n <= 7:
            return 3
        return 4

    month_cols = []  # (week_index, month_abbr)
    last_month = None
    cells = []
    for w in range(weeks):
        week_start = range_start + timedelta(days=w * 7)
        if week_start.month != last_month:
            month_cols.append((w, MONTH_ABBR_EN[week_start.month]))
            last_month = week_start.month
        for d_offset in range(7):
            cur = range_start + timedelta(days=w * 7 + d_offset)
            if cur > today:
                cells.append('<span class="heatmap-cell is-future" aria-hidden="true"></span>')
                continue
            n = counts.get(cur.isoformat(), 0)
            label = f"{plural(n, 'article')} on {DAY_NAMES_EN[cur.weekday()]}, {MONTH_NAMES_EN[cur.month]} {cur.day}, {cur.year}"
            cells.append(f'<span class="heatmap-cell level-{level_for(n)}" title="{escape(label)}" aria-label="{escape(label)}" role="img"></span>')

    month_labels_html = "".join(
        f'<span style="grid-column: {w + 1};">{name}</span>' for w, name in month_cols
    )

    return f"""
<section class="heatmap-section">
    <h2 class="heatmap-title">Activity over the last 12 months</h2>
    <div class="heatmap-scroll">
        <div class="heatmap" style="--weeks: {weeks};">
            <div class="heatmap-months">{month_labels_html}</div>
            <div class="heatmap-body">
                <div class="heatmap-daylabels">
                    <span></span><span>Mon</span><span></span><span>Wed</span><span></span><span>Fri</span><span></span>
                </div>
                <div class="heatmap-grid">{"".join(cells)}</div>
            </div>
        </div>
    </div>
    <div class="heatmap-legend">
        <span>Less</span>
        <span class="heatmap-cell level-0"></span>
        <span class="heatmap-cell level-1"></span>
        <span class="heatmap-cell level-2"></span>
        <span class="heatmap-cell level-3"></span>
        <span class="heatmap-cell level-4"></span>
        <span>More</span>
    </div>
</section>"""


def generate_index(articles):
    """Generate homepage with daily synthesis + recent articles."""
    # Group by date
    by_date = defaultdict(list)
    for a in articles:
        d = a["date_sort"]
        if re.match(r"\d{4}-\d{2}-\d{2}", d):
            by_date[d].append(a)

    # Sort dates descending
    sorted_dates = sorted(by_date.keys(), reverse=True)

    body_parts = []
    body_parts.append(f"""
<header class="hero">
    <h1>🗺️ {SITE_TITLE}</h1>
    <p class="subtitle">{SITE_SUBTITLE}</p>
    <p class="stats">{plural(len(articles), 'article')} · {plural(len(sorted_dates), 'day')} of watch</p>
</header>""")

    body_parts.append(generate_heatmap(articles))

    # Daily synthesis sections (show last 7 days with content)
    days_shown = 0
    max_days = 7
    for dt in sorted_dates:
        if days_shown >= max_days:
            break
        day_articles = by_date[dt]
        # Format date nicely
        try:
            d = datetime.strptime(dt, "%Y-%m-%d")
            date_en = f"{DAY_NAMES_EN[d.weekday()]}, {MONTH_NAMES_EN[d.month]} {d.day}, {d.year}"
        except:
            date_en = dt

        day_id = dt.replace("-", "")
        body_parts.append(f"""
<section class="daily-synthesis" id="day-{day_id}">
    <h2 class="day-header">
        <time datetime="{dt}">{date_en}</time>
        <span class="article-count">{plural(len(day_articles), 'article')}</span>
    </h2>
    <div class="day-articles">""")

        for a in day_articles:
            takeaways_html = ""
            if a["takeaways"]:
                takeaways_html = f'<details class="takeaways"><summary>Key takeaways</summary><ul>{"".join(f"<li>{escape(t)}</li>" for t in a["takeaways"])}</ul></details>'

            source_link = ""
            if a["source"]:
                source_link = f'<a href="{escape(a["source"])}" target="_blank" rel="noopener" class="source-link">→ Source article</a>'

            body_parts.append(f"""
        <article class="article-card">
            <h3><a href="{a["url"]}">{escape(a["title"])}</a></h3>
            <p class="elevator-pitch">{escape(a["elevator_pitch"])}</p>
            {takeaways_html}
            <div class="article-meta">
                <span class="meta-date">{escape(a["date"])}</span>
                {f'<span class="meta-author">{escape(a["author"])}</span>' if a["author"] and a["author"] != "Unknown" else ''}
                {source_link}
            </div>
        </article>""")

        body_parts.append("""
    </div>
</section>""")
        days_shown += 1

    # Link to archives
    body_parts.append("""
<div class="archives-link">
    <a href="archives.html" class="btn">📚 View all archives →</a>
</div>""")

    return page_html("Home", "\n".join(body_parts), nav_active="home")


def generate_article_page(article):
    """Generate individual article page (fiche de récap)."""
    # Articles live two levels deep (articles/YYYY-MM/slug.html) unless the
    # date couldn't be parsed from the filename, in which case they sit one
    # level deep (articles/slug.html).
    base = "../../" if (article["year"] and article["month"]) else "../"

    body_parts = []
    body_parts.append(f"""
<article class="article-full">
    <a href="{base}index.html" class="back-link">← Back home</a>
    <h1>{escape(article["title"])}</h1>
    <div class="article-meta-full">
        <span class="meta-date">📅 {escape(article["date"])}</span>
        {f'<span class="meta-author">✍️ {escape(article["author"])}</span>' if article["author"] and article["author"] != "Unknown" else ''}
        {f'<span class="meta-keywords">🏷️ {escape(article["keywords"])}</span>' if article["keywords"] and article["keywords"] != "Unknown" else ''}
    </div>""")

    if article["source"]:
        body_parts.append(f"""
    <a href="{escape(article["source"])}" target="_blank" rel="noopener" class="source-link-full">
        🔗 Read the source article →
    </a>""")

    if article["elevator_pitch"]:
        body_parts.append(f"""
    <section class="elevator-pitch-section">
        <h2>💡 Quick summary</h2>
        <p class="elevator-pitch">{escape(article["elevator_pitch"])}</p>
    </section>""")

    if article["takeaways"]:
        body_parts.append("""
    <section class="takeaways-section">
        <h2>📌 Key takeaways</h2>
        <ul class="takeaways-list">""")
        for t in article["takeaways"]:
            body_parts.append(f"            <li>{escape(t)}</li>")
        body_parts.append("""        </ul>
    </section>""")

    if article["source"]:
        body_parts.append(f"""
    <a href="{escape(article["source"])}" target="_blank" rel="noopener" class="source-link-full">
        🔗 Read the full article on the source site →
    </a>""")

    body_parts.append("""
</article>""")

    return page_html(article["title"], "\n".join(body_parts), base=base)


def generate_archives(articles):
    """Generate archives page grouped by year/month."""
    # Group by year-month
    by_month = defaultdict(list)
    for a in articles:
        if a["year"] and a["month"]:
            key = f"{a['year']}-{a['month']}"
            by_month[key].append(a)

    sorted_months = sorted(by_month.keys(), reverse=True)

    body_parts = []
    body_parts.append("""
<header class="page-header">
    <h1>📚 Archives</h1>
    <p>All articles from the mapping watch</p>
</header>""")

    current_year = ""
    for ym in sorted_months:
        year, month = ym.split("-")
        if year != current_year:
            if current_year:
                body_parts.append("</div>")
            current_year = year
            body_parts.append(f"""
<div class="archive-year">
    <h2>{year}</h2>""")

        month_name = MONTH_NAMES_EN.get(int(month), month)
        month_articles = by_month[ym]

        body_parts.append(f"""
    <div class="archive-month">
        <h3>{month_name} ({plural(len(month_articles), 'article')})</h3>
        <ul class="archive-list">""")

        for a in month_articles:
            body_parts.append(f"""
            <li>
                <a href="{a["url"]}">{escape(a["title"])}</a>
                <span class="archive-date">{escape(a["date"])}</span>
            </li>""")

        body_parts.append("""
        </ul>
    </div>""")

    if current_year:
        body_parts.append("</div>")

    return page_html("Archives", "\n".join(body_parts), nav_active="archives")


def generate_rss(articles):
    """Generate RSS 2.0 feed."""
    parts = [f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
<channel>
    <title>{escape(SITE_TITLE)}</title>
    <link>{SITE_URL}</link>
    <description>{escape(SITE_DESCRIPTION)}</description>
    <language>{SITE_LANG}</language>
    <atom:link href="{SITE_URL}/feed.xml" rel="self" type="application/rss+xml"/>
    <lastBuildDate>{datetime.now(tz=__import__('datetime').timezone.utc).strftime("%a, %d %b %Y %H:%M:%S +0000")}</lastBuildDate>"""]

    # Include last 50 articles
    for a in articles[:50]:
        title = escape(a["title"])
        link = f"{SITE_URL}/{a['url']}"
        desc_parts = []
        if a["elevator_pitch"]:
            desc_parts.append(a["elevator_pitch"])
        if a["takeaways"]:
            desc_parts.append("Key takeaways: " + " ; ".join(a["takeaways"]))
        if a["synthesis"]:
            # First 300 chars of synthesis
            desc_parts.append(a["synthesis"][:300] + "..." if len(a["synthesis"]) > 300 else a["synthesis"])
        description = " — ".join(desc_parts[:2]) if desc_parts else a["title"]
        description = escape(description)

        pub_date = ""
        if re.match(r"\d{4}-\d{2}-\d{2}", a["date_sort"]):
            try:
                d = datetime.strptime(a["date_sort"], "%Y-%m-%d")
                pub_date = d.strftime("%a, %d %b %Y %H:%M:%S +0000")
            except:
                pub_date = datetime.now(tz=__import__('datetime').timezone.utc).strftime("%a, %d %b %Y %H:%M:%S +0000")
        else:
            pub_date = datetime.now(tz=__import__('datetime').timezone.utc).strftime("%a, %d %b %Y %H:%M:%S +0000")

        parts.append(f"""
    <item>
        <title>{title}</title>
        <link>{link}</link>
        <guid isPermaLink="true">{link}</guid>
        <description>{description}</description>
        <pubDate>{pub_date}</pubDate>
    </item>""")

    parts.append("""
</channel>
</rss>""")
    return "\n".join(parts)


# ─── CSS ──────────────────────────────────────────────────────────────────────

CSS = """/* Mapping Forward — Static Site Stylesheet */
:root {
    --bg: #0f1117;
    --bg-card: #1a1d28;
    --bg-hover: #222636;
    --text: #e0e0e8;
    --text-muted: #8888a0;
    --accent: #4a9eff;
    --accent-hover: #6bb0ff;
    --border: #2a2d3a;
    --radius: 8px;
    --max-width: 900px;
}
@media (prefers-color-scheme: light) {
    :root {
        --bg: #fafafa;
        --bg-card: #ffffff;
        --bg-hover: #f0f0f5;
        --text: #1a1a2e;
        --text-muted: #666;
        --accent: #2563eb;
        --accent-hover: #1d4ed8;
        --border: #e0e0e8;
    }
}
* { margin: 0; padding: 0; box-sizing: border-box; }
body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    background: var(--bg);
    color: var(--text);
    line-height: 1.6;
    font-size: 16px;
}
a { color: var(--accent); text-decoration: none; }
a:hover { color: var(--accent-hover); text-decoration: underline; }

/* Navbar */
.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1rem 2rem;
    background: var(--bg-card);
    border-bottom: 1px solid var(--border);
    position: sticky;
    top: 0;
    z-index: 100;
    backdrop-filter: blur(10px);
}
.nav-brand a { font-size: 1.2rem; font-weight: 700; color: var(--text); }
.nav-brand a:hover { text-decoration: none; }
.nav-links { display: flex; gap: 1.5rem; }
.nav-links a { color: var(--text-muted); font-size: 0.95rem; }
.nav-links a:hover, .nav-links a.active { color: var(--accent); }

/* Main */
main {
    max-width: var(--max-width);
    margin: 0 auto;
    padding: 2rem 1rem;
}

/* Hero */
.hero {
    text-align: center;
    padding: 3rem 1rem;
}
.hero h1 { font-size: 2.5rem; margin-bottom: 0.5rem; }
.subtitle { color: var(--text-muted); font-size: 1.2rem; }
.stats { color: var(--text-muted); font-size: 0.9rem; margin-top: 0.5rem; }

/* Activity heatmap */
.heatmap-section { margin: 0 0 3rem; }
.heatmap-title {
    font-size: 1rem;
    font-weight: 600;
    color: var(--text-muted);
    margin-bottom: 0.8rem;
    text-align: center;
}
.heatmap-scroll { overflow-x: auto; padding-bottom: 0.25rem; }
.heatmap { display: inline-flex; flex-direction: column; gap: 0.3rem; margin: 0 auto; }
.heatmap-months {
    display: grid;
    grid-template-columns: repeat(var(--weeks), 13px);
    gap: 3px;
    margin-left: 28px;
    font-size: 0.7rem;
    color: var(--text-muted);
}
.heatmap-body { display: flex; gap: 4px; }
.heatmap-daylabels {
    display: grid;
    grid-template-rows: repeat(7, 13px);
    gap: 3px;
    width: 24px;
    font-size: 0.65rem;
    color: var(--text-muted);
    text-align: right;
    line-height: 13px;
}
.heatmap-grid {
    display: grid;
    grid-template-columns: repeat(var(--weeks), 13px);
    grid-template-rows: repeat(7, 13px);
    grid-auto-flow: column;
    gap: 3px;
}
.heatmap-cell {
    width: 13px;
    height: 13px;
    border-radius: 3px;
    border: 1px solid var(--border);
    background: var(--bg-card);
}
.heatmap-cell.level-1 { background: color-mix(in srgb, var(--accent) 25%, var(--bg-card)); border-color: transparent; }
.heatmap-cell.level-2 { background: color-mix(in srgb, var(--accent) 50%, var(--bg-card)); border-color: transparent; }
.heatmap-cell.level-3 { background: color-mix(in srgb, var(--accent) 75%, var(--bg-card)); border-color: transparent; }
.heatmap-cell.level-4 { background: var(--accent); border-color: transparent; }
.heatmap-cell.is-future { background: transparent; border-color: transparent; }
.heatmap-legend {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0.3rem;
    margin-top: 0.6rem;
    font-size: 0.75rem;
    color: var(--text-muted);
}
.heatmap-legend .heatmap-cell { width: 11px; height: 11px; }

/* Daily synthesis */
.daily-synthesis {
    margin-bottom: 3rem;
    border-bottom: 1px solid var(--border);
    padding-bottom: 2rem;
}
.day-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 1.5rem;
}
.day-header h2 { font-size: 1.4rem; }
.article-count {
    background: var(--bg-card);
    color: var(--text-muted);
    padding: 0.2rem 0.8rem;
    border-radius: 20px;
    font-size: 0.85rem;
}

/* Article card */
.article-card {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 1.5rem;
    margin-bottom: 1rem;
    transition: border-color 0.2s;
}
.article-card:hover { border-color: var(--accent); }
.article-card h3 { margin-bottom: 0.5rem; font-size: 1.15rem; }
.article-card h3 a { color: var(--text); }
.article-card h3 a:hover { color: var(--accent); }
.elevator-pitch { color: var(--text-muted); font-size: 0.95rem; margin-bottom: 0.8rem; }
.article-meta {
    display: flex;
    gap: 1rem;
    flex-wrap: wrap;
    font-size: 0.85rem;
    color: var(--text-muted);
}
.source-link { font-weight: 500; }

/* Takeaways (inline) */
details.takeaways {
    margin: 0.8rem 0;
    font-size: 0.9rem;
}
details.takeaways summary {
    cursor: pointer;
    color: var(--accent);
    font-weight: 500;
}
details.takeaways ul { margin-top: 0.5rem; padding-left: 1.5rem; }
details.takeaways li { color: var(--text-muted); margin-bottom: 0.3rem; }

/* Article full page */
.article-full { padding: 1rem 0; }
.back-link { display: inline-block; margin-bottom: 1.5rem; font-size: 0.9rem; }
.article-full h1 { font-size: 2rem; margin-bottom: 1rem; line-height: 1.3; }
.article-meta-full {
    display: flex;
    gap: 1.5rem;
    flex-wrap: wrap;
    color: var(--text-muted);
    font-size: 0.9rem;
    margin-bottom: 1.5rem;
}
.source-link-full {
    display: inline-block;
    background: var(--accent);
    color: #fff !important;
    padding: 0.6rem 1.5rem;
    border-radius: var(--radius);
    font-weight: 500;
    margin: 1rem 0 2rem;
    transition: background 0.2s;
}
.source-link-full:hover { background: var(--accent-hover); text-decoration: none; }

.elevator-pitch-section, .takeaways-section, .synthesis-section {
    margin-bottom: 2rem;
}
.elevator-pitch-section h2, .takeaways-section h2, .synthesis-section h2 {
    font-size: 1.3rem;
    margin-bottom: 0.8rem;
    border-bottom: 2px solid var(--border);
    padding-bottom: 0.3rem;
}
.elevator-pitch-section .elevator-pitch {
    font-size: 1.1rem;
    color: var(--text);
    font-style: italic;
}
.takeaways-list { padding-left: 1.5rem; }
.takeaways-list li { margin-bottom: 0.5rem; }
.synthesis-content p { margin-bottom: 1rem; }
.synthesis-content ul { padding-left: 1.5rem; margin-bottom: 1rem; }

/* Archives */
.page-header { text-align: center; padding: 2rem 0 3rem; }
.page-header h1 { font-size: 2rem; }
.page-header p { color: var(--text-muted); margin-top: 0.5rem; }
.archive-year { margin-bottom: 2rem; }
.archive-year h2 { font-size: 1.5rem; margin-bottom: 1rem; }
.archive-month { margin-bottom: 1.5rem; }
.archive-month h3 { font-size: 1.1rem; margin-bottom: 0.5rem; color: var(--text-muted); }
.archive-list { list-style: none; }
.archive-list li {
    padding: 0.5rem 0;
    border-bottom: 1px solid var(--border);
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 1rem;
}
.archive-list li a { flex: 1; }
.archive-date { color: var(--text-muted); font-size: 0.85rem; white-space: nowrap; }

/* Buttons */
.btn {
    display: inline-block;
    background: var(--accent);
    color: #fff !important;
    padding: 0.8rem 2rem;
    border-radius: var(--radius);
    font-weight: 500;
    transition: background 0.2s;
}
.btn:hover { background: var(--accent-hover); text-decoration: none; }
.archives-link { text-align: center; margin: 3rem 0; }

/* Footer */
.site-footer {
    text-align: center;
    padding: 2rem;
    border-top: 1px solid var(--border);
    color: var(--text-muted);
    font-size: 0.85rem;
}
.site-footer a { color: var(--accent); }

/* Responsive */
@media (max-width: 768px) {
    .navbar { flex-direction: column; gap: 0.5rem; padding: 1rem; }
    .nav-links { gap: 1rem; }
    .hero h1 { font-size: 1.8rem; }
    .day-header { flex-direction: column; align-items: flex-start; gap: 0.3rem; }
    .article-card { padding: 1rem; }
    .archive-list li { flex-direction: column; align-items: flex-start; }
    .heatmap-scroll { margin: 0 -1rem; padding: 0 1rem 0.25rem; }
}
"""


# ─── Main build ───────────────────────────────────────────────────────────────

def main():
    print("Loading articles...")
    articles = load_all_articles()
    print(f"  Found {len(articles)} articles")

    # Clean dist
    if os.path.exists(DIST_DIR):
        import shutil
        shutil.rmtree(DIST_DIR)
    os.makedirs(DIST_DIR)

    # Write CSS
    with open(os.path.join(DIST_DIR, "style.css"), "w") as f:
        f.write(CSS)
    print("  ✓ style.css")

    # Generate index.html
    index_html = generate_index(articles)
    with open(os.path.join(DIST_DIR, "index.html"), "w") as f:
        f.write(index_html)
    print("  ✓ index.html")

    # Generate article pages
    articles_dir = os.path.join(DIST_DIR, "articles")
    os.makedirs(articles_dir)
    for a in articles:
        # Create year-month subdirectory
        if a["year"] and a["month"]:
            subdir = os.path.join(articles_dir, f"{a['year']}-{a['month']}")
        else:
            subdir = articles_dir
        os.makedirs(subdir, exist_ok=True)
        html_path = os.path.join(subdir, f"{a['slug']}.html")
        with open(html_path, "w") as f:
            f.write(generate_article_page(a))
    print(f"  ✓ {len(articles)} article pages")

    # Generate archives.html
    archives_html = generate_archives(articles)
    with open(os.path.join(DIST_DIR, "archives.html"), "w") as f:
        f.write(archives_html)
    print("  ✓ archives.html")

    # Generate RSS feed
    rss = generate_rss(articles)
    with open(os.path.join(DIST_DIR, "feed.xml"), "w") as f:
        f.write(rss)
    print("  ✓ feed.xml")

    # Generate a JSON manifest (useful for integrations)
    manifest = {
        "site": SITE_TITLE,
        "url": SITE_URL,
        "generated": datetime.now().isoformat(),
        "article_count": len(articles),
        "articles": [
            {
                "title": a["title"],
                "url": f"{SITE_URL}/{a['url']}",
                "date": a["date"],
                "source": a["source"],
                "author": a["author"],
                "keywords": a["keywords"],
                "elevator_pitch": a["elevator_pitch"],
            }
            for a in articles
        ],
    }
    with open(os.path.join(DIST_DIR, "manifest.json"), "w") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
    print("  ✓ manifest.json")

    print(f"\nDone! Site generated in {DIST_DIR}")
    print(f"Open with: python3 -m http.server -d {DIST_DIR} 8000")


if __name__ == "__main__":
    main()
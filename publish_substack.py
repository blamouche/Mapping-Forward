#!/usr/bin/env python3
"""Publish a Substack post using Playwright with persistent Chrome profile."""
import json
import re
import sys
import time
from pathlib import Path
from playwright.sync_api import sync_playwright

POST_FILE = Path(__file__).parent / "substack" / "20261001-post-the-map-at-work.md"
SUBSTACK_URL = "https://mappingforward.substack.com"
PUBLISH_URL = "https://mappingforward.substack.com/publish/post"

def parse_markdown(md_text):
    """Parse the markdown file into title, subtitle, body HTML, and sources."""
    lines = md_text.strip().split('\n')
    title = None
    subtitle = None
    body_lines = []
    in_sources = False
    past_separator = False

    i = 0
    while i < len(lines):
        line = lines[i]
        if title is None and line.startswith('# '):
            title = line[2:].strip()
            i += 1
            continue
        if title and subtitle is None:
            stripped = line.strip()
            if stripped.startswith('*') and stripped.endswith('*') and not stripped.startswith('**'):
                subtitle = stripped[1:-1].strip()
                i += 1
                continue
            elif stripped == '':
                i += 1
                continue
            else:
                # No subtitle found, continue
                pass
        if line.strip() == '---':
            past_separator = True
            i += 1
            continue
        if past_separator and line.strip().startswith('## Sources'):
            in_sources = True
            i += 1
            continue
        if not in_sources and past_separator == False:
            body_lines.append(line)
        elif not in_sources and past_separator:
            # We're between subtitle and --- separator
            body_lines.append(line)
        i += 1

    body_md = '\n'.join(body_lines).strip()
    return title, subtitle, body_md

def markdown_to_html(md_text):
    """Convert simple markdown to HTML for Substack editor."""
    lines = md_text.split('\n')
    html_parts = []
    in_list = False
    in_paragraph = []

    def flush_paragraph():
        nonlocal in_paragraph
        if in_paragraph:
            text = ' '.join(in_paragraph).strip()
            if text:
                text = convert_links(text)
                html_parts.append(f'<p>{text}</p>')
            in_paragraph = []

    for line in lines:
        stripped = line.strip()
        if stripped.startswith('## '):
            flush_paragraph()
            if in_list:
                html_parts.append('</ul>')
                in_list = False
            heading = stripped[3:].strip()
            heading = convert_links(heading)
            html_parts.append(f'<h2>{heading}</h2>')
        elif stripped.startswith('- '):
            flush_paragraph()
            if not in_list:
                html_parts.append('<ul>')
                in_list = True
            item = stripped[2:].strip()
            item = convert_links(item)
            html_parts.append(f'<li>{item}</li>')
        elif stripped == '':
            flush_paragraph()
            if in_list:
                html_parts.append('</ul>')
                in_list = False
        else:
            if in_list:
                html_parts.append('</ul>')
                in_list = False
            in_paragraph.append(stripped)

    flush_paragraph()
    if in_list:
        html_parts.append('</ul>')

    return '\n'.join(html_parts)

def convert_links(text):
    """Convert [text](url) to <a href="url">text</a>."""
    return re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', text)

def main():
    md_text = POST_FILE.read_text()
    title, subtitle, body_md = parse_markdown(md_text)
    body_html = markdown_to_html(body_md)

    print(f"Title: {title}")
    print(f"Subtitle: {subtitle}")
    print(f"Body HTML length: {len(body_html)} chars")
    print(f"---")

    chrome_profile = str(Path.home() / "Library/Application Support/Google/Chrome")

    with sync_playwright() as p:
        # Launch Chromium with persistent context using Chrome's profile
        browser = p.chromium.launch_persistent_context(
            user_data_dir=chrome_profile,
            channel="chrome",
            headless=False,
            args=['--disable-blink-features=AutomationControlled'],
        )

        page = browser.new_page()

        # Navigate to publish page
        print("Navigating to publish page...")
        page.goto(PUBLISH_URL, wait_until="networkidle", timeout=30000)
        time.sleep(3)

        current_url = page.url
        print(f"Current URL: {current_url}")

        # Check if we need to log in
        if "login" in current_url.lower() or "account" in current_url.lower():
            print("NOT_LOGGED_IN: Substack requires login")
            browser.close()
            sys.exit(1)

        # Check if the editor loaded
        title_el = page.query_selector('textarea.pencraft.page-title')
        if not title_el:
            print("NO_EDITOR: Could not find title field")
            # Take screenshot for debugging
            page.screenshot(path="/tmp/substack_no_editor.png")
            browser.close()
            sys.exit(1)

        # Fill in title
        print("Filling title...")
        page.evaluate('''(title) => {
            const el = document.querySelector('textarea.pencraft.page-title');
            el.value = title;
            el.dispatchEvent(new Event('input', {bubbles: true}));
            el.dispatchEvent(new Event('change', {bubbles: true}));
        }''', title)
        time.sleep(1)

        # Fill in subtitle
        if subtitle:
            print("Filling subtitle...")
            subtitle_el = page.query_selector('textarea.pencraft.subtitle')
            if subtitle_el:
                page.evaluate('''(subtitle) => {
                    const el = document.querySelector('textarea.pencraft.subtitle');
                    el.value = subtitle;
                    el.dispatchEvent(new Event('input', {bubbles: true}));
                    el.dispatchEvent(new Event('change', {bubbles: true}));
                }''', subtitle)
                time.sleep(1)

        # Insert body content
        print("Inserting body content...")
        editor = page.query_selector('.tiptap.ProseMirror')
        if editor:
            page.evaluate('''() => { document.querySelector('.tiptap.ProseMirror').focus(); }''')
            time.sleep(0.5)
            page.evaluate('''() => { document.execCommand('selectAll', false, null); }''')
            time.sleep(0.3)
            page.evaluate('''(html) => { document.execCommand('insertHTML', false, html); }''', body_html)
            time.sleep(2)
        else:
            print("NO_EDITOR: Could not find ProseMirror editor")
            page.screenshot(path="/tmp/substack_no_editor_body.png")
            browser.close()
            sys.exit(1)

        # Wait for save
        print("Waiting for save...")
        time.sleep(5)
        page.screenshot(path="/tmp/substack_after_content.png")

        # Click Continue/Continuer button
        print("Looking for Continue button...")
        continuer_btn = None
        # Try French and English
        for selector in ['button:has-text("Continuer")', 'button:has-text("Continue")']:
            try:
                btn = page.wait_for_selector(selector, timeout=5000)
                if btn:
                    continuer_btn = btn
                    break
            except:
                continue

        if continuer_btn:
            print("Clicking Continue...")
            continuer_btn.click()
            time.sleep(5)
            page.screenshot(path="/tmp/substack_publish_screen.png")
        else:
            print("NO_CONTINUE_BUTTON: Could not find Continue button")
            page.screenshot(path="/tmp/substack_no_continue.png")
            browser.close()
            sys.exit(1)

        # Look for "Envoyer à tous maintenant" / "Send to everyone now"
        print("Looking for publish button...")
        publish_btn = None
        for selector in ['button:has-text("Envoyer à tous maintenant")', 'button:has-text("Send to everyone now")', 'button:has-text("Publish")']:
            try:
                btn = page.wait_for_selector(selector, timeout=10000)
                if btn:
                    publish_btn = btn
                    break
            except:
                continue

        if publish_btn:
            print("Clicking publish button...")
            publish_btn.click()
            time.sleep(3)

            # Handle possible dialog about subscription buttons
            for dialog_sel in ['button:has-text("Publier sans boutons")', 'button:has-text("Publish without buttons")']:
                try:
                    dialog_btn = page.wait_for_selector(dialog_sel, timeout=5000)
                    if dialog_btn:
                        print("Clicking publish without buttons...")
                        dialog_btn.click()
                        time.sleep(3)
                        break
                except:
                    continue

            time.sleep(5)
            page.screenshot(path="/tmp/substack_published.png")
            print(f"Final URL: {page.url}")

            # Check if published
            if "publish/posts/detail" in page.url or "Publié" in page.content():
                print("PUBLISHED_SUCCESS")
            else:
                print(f"Publish status unclear. URL: {page.url}")
        else:
            print("NO_PUBLISH_BUTTON: Could not find publish button")
            page.screenshot(path="/tmp/substack_no_publish.png")

        browser.close()

if __name__ == '__main__':
    main()
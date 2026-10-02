#!/usr/bin/env python3
"""Publish a Substack post via Playwright CDP to Chrome with openclaw profile."""
import json
import re
import sys
import time
from pathlib import Path
from playwright.sync_api import sync_playwright

POST_FILE = Path(__file__).parent / "substack" / "20261001-post-the-map-at-work.md"
CDP_URL = "http://localhost:9224"
PUBLISH_URL = "https://mappingforward.substack.com/publish/post"

def parse_markdown(md_text):
    lines = md_text.strip().split('\n')
    title = None
    subtitle = None
    body_lines = []
    found_separator = False
    i = 0
    while i < len(lines):
        line = lines[i]
        if title is None and line.startswith('# '):
            title = line[2:].strip()
            i += 1
            continue
        if title and subtitle is None:
            stripped = line.strip()
            if stripped.startswith('*') and not stripped.startswith('**') and stripped.endswith('*'):
                subtitle = stripped[1:-1].strip()
                i += 1
                continue
            elif stripped == '':
                i += 1
                continue
        if line.strip() == '---':
            found_separator = True
            i += 1
            continue
        if found_separator:
            i += 1
            continue
        if title and subtitle:
            body_lines.append(line)
        i += 1
    body_md = '\n'.join(body_lines).strip()
    return title, subtitle, body_md

def convert_links(text):
    return re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', text)

def markdown_to_html(md_text):
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
            heading = convert_links(stripped[3:].strip())
            html_parts.append(f'<h2>{heading}</h2>')
        elif stripped.startswith('- '):
            flush_paragraph()
            if not in_list:
                html_parts.append('<ul>')
                in_list = True
            html_parts.append(f'<li>{convert_links(stripped[2:].strip())}</li>')
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

def main():
    md_text = POST_FILE.read_text()
    title, subtitle, body_md = parse_markdown(md_text)
    body_html = markdown_to_html(body_md)

    print(f"Title: {title}")
    print(f"Subtitle: {subtitle}")
    print(f"Body HTML length: {len(body_html)} chars")

    with sync_playwright() as p:
        print(f"Connecting to Chrome on {CDP_URL}...")
        browser = p.chromium.connect_over_cdp(CDP_URL)
        context = browser.contexts[0]
        pages = context.pages
        print(f"Found {len(pages)} existing pages")

        page = context.new_page()

        print(f"Navigating to {PUBLISH_URL}...")
        page.goto(PUBLISH_URL, wait_until="networkidle", timeout=30000)
        time.sleep(5)

        current_url = page.url
        print(f"Current URL: {current_url}")

        if "sign-in" in current_url.lower() or "login" in current_url.lower():
            print("NOT_LOGGED_IN: Substack requires login")
            page.screenshot(path="/tmp/substack_login_needed.png")
            browser.close()
            sys.exit(1)

        # Check if editor loaded
        title_el = page.query_selector('textarea.pencraft.page-title')
        if not title_el:
            title_el = page.query_selector('[data-testid="editor-title"]')
            if not title_el:
                print("NO_EDITOR: Could not find title field")
                page.screenshot(path="/tmp/substack_no_editor.png")
                print(f"Page title: {page.title()}")
                browser.close()
                sys.exit(1)

        # Fill title
        print("Filling title...")
        page.evaluate('''(title) => {
            const el = document.querySelector('textarea.pencraft.page-title') || document.querySelector('[data-testid="editor-title"]');
            el.value = title;
            el.dispatchEvent(new Event('input', {bubbles: true}));
            el.dispatchEvent(new Event('change', {bubbles: true}));
        }''', title)
        time.sleep(1)

        # Fill subtitle
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

        # Insert body
        print("Inserting body content...")
        editor = page.query_selector('.tiptap.ProseMirror')
        if editor:
            page.evaluate('''() => { document.querySelector('.tiptap.ProseMirror').focus(); }''')
            time.sleep(0.5)
            page.evaluate('''() => { document.execCommand('selectAll', false, null); }''')
            time.sleep(0.3)
            page.evaluate('''(html) => { document.execCommand('insertHTML', false, html); }''', body_html)
            time.sleep(3)
        else:
            print("NO_EDITOR: Could not find ProseMirror editor")
            browser.close()
            sys.exit(1)

        print("Waiting for save...")
        time.sleep(5)
        page.screenshot(path="/tmp/substack_after_content.png")

        # Click Continue
        print("Looking for Continue button...")
        continuer_btn = None
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
            print("NO_CONTINUE_BUTTON")
            page.screenshot(path="/tmp/substack_no_continue.png")
            browser.close()
            sys.exit(1)

        # Click publish
        print("Looking for publish button...")
        publish_btn = None
        for selector in ['button:has-text("Envoyer à tous maintenant")', 'button:has-text("Send to everyone now")']:
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

            if "publish/posts/detail" in page.url:
                print("PUBLISHED_SUCCESS")
            else:
                print(f"Publish status unclear. URL: {page.url}")
        else:
            print("NO_PUBLISH_BUTTON")
            page.screenshot(path="/tmp/substack_no_publish.png")

        browser.close()

if __name__ == '__main__':
    main()
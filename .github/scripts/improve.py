#!/usr/bin/env python3
"""Autonomous Brain Dump app improvement agent — runs in GitHub Actions."""
import urllib.request, urllib.error, json, os, re, base64, datetime

ANTHROPIC_KEY = os.environ.get('ANTHROPIC_API_KEY', '')
REPO = 'besutohai-dotcom/brain-dump'
GH_TOKEN = os.environ.get('GITHUB_TOKEN', '')

def read_file(path):
    with open(path, 'r') as f:
        return f.read()

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True) if '/' in path else None
    with open(path, 'w') as f:
        f.write(content)

def call_claude(prompt, max_tokens=4096):
    req = urllib.request.Request(
        'https://api.anthropic.com/v1/messages',
        data=json.dumps({
            'model': 'claude-opus-4-7',
            'max_tokens': max_tokens,
            'thinking': {'type': 'adaptive'},
            'messages': [{'role': 'user', 'content': prompt}]
        }).encode(),
        headers={
            'Content-Type': 'application/json',
            'x-api-key': ANTHROPIC_KEY,
            'anthropic-version': '2023-06-01',
        },
        method='POST'
    )
    resp = urllib.request.urlopen(req, timeout=120)
    data = json.loads(resp.read())
    # Extract text from content blocks (skip thinking blocks)
    for block in data['content']:
        if block.get('type') == 'text':
            return block['text']
    return ''

def main():
    today = datetime.date.today().isoformat()
    app_html = read_file('index.html')
    roadmap = read_file('ROADMAP.md')

    # Find next planned item
    planned = re.findall(r'- \[ \] (.+)', roadmap)
    if not planned:
        print('No planned items found in roadmap.')
        return
    next_item = planned[0]
    print(f'Implementing: {next_item}')

    prompt = f"""You are improving a Japanese-language Brain Dump PWA app. It's a single HTML file using Preact 10 + htm via esm.sh CDN.

CURRENT TASK TO IMPLEMENT: {next_item}

CONSTRAINTS:
- Single HTML file only — no external JS files, no build step needed
- Use Preact h() function calls (NOT JSX, NOT tagged templates — just h('tag', {{props}}, children))
- Match existing code style exactly
- Japanese UI text for all user-facing strings
- Keep all existing features working
- Mobile-first design, works at 390px width
- The app uses localStorage key 'brain-dump-v1' with schema: {{tasks:[], categories:[], apiKey:''}}
- Task schema: {{id, originalText, title, category, nextActions:[], createdAt, status:'active'|'done'}}

CURRENT APP CODE:
```html
{app_html[:12000]}
```

Return ONLY the complete updated HTML file with the improvement implemented. No explanation, no markdown code fences — just the raw HTML starting with <!DOCTYPE html>."""

    print('Calling Claude...')
    result = call_claude(prompt)

    # Extract HTML (remove any accidental markdown fences)
    result = result.strip()
    if result.startswith('```'):
        result = re.sub(r'^```[^\n]*\n', '', result)
        result = re.sub(r'\n```$', '', result.strip())

    if not result.startswith('<!DOCTYPE html>') and not result.startswith('<!doctype html>'):
        print(f'ERROR: Response does not look like HTML. First 200 chars:\n{result[:200]}')
        return

    write_file('index.html', result)
    print('index.html updated.')

    # Update ROADMAP.md
    updated_roadmap = roadmap.replace(
        f'- [ ] {next_item}',
        f'- [x] {next_item}'
    )
    # Move to Done section
    updated_roadmap = updated_roadmap.replace(
        '## ✅ Done',
        f'## ✅ Done\n- [x] {next_item}'
    ).replace(f'- [x] {next_item}\n- [x] {next_item}', f'- [x] {next_item}')

    # Update last-updated date
    updated_roadmap = re.sub(r'Last updated: .+', f'Last updated: {today}', updated_roadmap)

    # Add to test log
    log_entry = f'| {today} | Implemented: {next_item} | Verified HTML output | ✅ |'
    updated_roadmap = updated_roadmap.replace(
        '| Date | Input | Categorized As | Status |',
        f'| Date | Input | Categorized As | Status |\n{log_entry}'
    )

    # Add to change log
    updated_roadmap += f'\n- {today}: {next_item}\n'

    write_file('ROADMAP.md', updated_roadmap)
    print('ROADMAP.md updated.')
    print(f'Done: {next_item}')

if __name__ == '__main__':
    main()

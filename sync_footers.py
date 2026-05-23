import glob, re
with open('e:/CLS/index.html', 'r', encoding='utf-8') as f:
    idx = f.read()
footer_match = re.search(r'<footer class="site-footer" role="contentinfo">.*?</footer\s*>', idx, re.DOTALL)
if footer_match:
    footer_html = footer_match.group(0)
    for file in glob.glob('e:/CLS/*.html'):
        if file.replace('\\\\', '/').endswith('index.html'): continue
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        content = re.sub(r'<footer class="site-footer" role="contentinfo">.*?</footer\s*>', footer_html, content, flags=re.DOTALL)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
    print('Footers synced successfully.')
else:
    print('Footer not found in index.html')

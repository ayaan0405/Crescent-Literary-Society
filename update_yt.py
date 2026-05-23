import glob

html_files = glob.glob("e:/CLS/*.html")

yt_html = """<div class="footer-contact-item">
<svg aria-hidden="true" class="footer-contact-icon" viewBox="0 0 24 24"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"></path></svg>
<a href="https://www.youtube.com/@crescentliterarysociety" rel="noopener" target="_blank">www.youtube.com/@crescentliterarysociety</a>
</div>"""

target_string = """<a href="https://facebook.com/crescentlitsociety" rel="noopener" target="_blank">/crescentlitsociety</a>
</div>"""

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if "www.youtube.com/@crescentliterarysociety" not in content:
        if target_string in content:
            content = content.replace(target_string, target_string + "\n" + yt_html)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Updated footers with youtube in all HTML files.")

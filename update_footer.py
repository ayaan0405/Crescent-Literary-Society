import glob
import re

html_files = glob.glob("e:/CLS/*.html")

yt_html = """<div class="footer-contact-item">
<svg aria-hidden="true" class="footer-contact-icon" viewBox="0 0 24 24"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"></path></svg>
<a href="https://www.youtube.com/@crescentliterarysociety" rel="noopener" target="_blank">www.youtube.com/@crescentliterarysociety</a>
</div>"""

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # 1. Add Youtube link
    if "www.youtube.com/@crescentliterarysociety" not in content:
        fb_pattern = re.compile(r'(<div class="footer-contact-item">\s*<svg.*?</svg>\s*<a href="https://facebook\.com/crescentlitsociety".*?</a>\s*</div>)', re.DOTALL)
        content = fb_pattern.sub(r'\1\n' + yt_html, content)
        
    # 2. Swap motto and copyright
    copyright_pattern = re.compile(r'<p class="footer-copyright">.*?</p>', re.DOTALL)
    motto_pattern = re.compile(r'<p class="footer-motto">.*?</p>', re.DOTALL)
    istd_pattern = re.compile(r'<p class="footer-istd".*?</p>', re.DOTALL)
    
    copyright_match = copyright_pattern.search(content)
    motto_match = motto_pattern.search(content)
    istd_match = istd_pattern.search(content)
    
    if copyright_match and motto_match and istd_match:
        c_str = copyright_match.group(0)
        m_str = motto_match.group(0)
        i_str = istd_match.group(0)
        
        inner_pattern = re.compile(r'(<div class="footer-bottom-inner">)(.*?)(</div>\s*</div>\s*</div>\s*</footer>)', re.DOTALL)
        
        def replacement(m):
            new_inner = f"\n{m_str}\n{i_str}\n{c_str}\n"
            return m.group(1) + new_inner + m.group(3)
            
        content = inner_pattern.sub(replacement, content)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Updated footers in all HTML files.")

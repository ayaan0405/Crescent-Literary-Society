import glob, re

files = glob.glob('e:/CLS/*.html')
yt_link = '<a href="https://www.youtube.com/@crescentliterarysociety" target="_blank" rel="noopener" class="footer-social-link" aria-label="YouTube" id="footer-youtube"><svg viewBox="0 0 24 24"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg></a>'

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    if 'id="footer-youtube"' in content:
        # replace the existing youtube link
        content = re.sub(r'<a[^>]*id="footer-youtube"[^>]*>.*?</a>', yt_link, content, flags=re.DOTALL)
    else:
        # insert after facebook link
        content = re.sub(r'(<a[^>]*id="footer-facebook"[^>]*>.*?</a>)', r'\1\n              ' + yt_link, content, flags=re.DOTALL)
        
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

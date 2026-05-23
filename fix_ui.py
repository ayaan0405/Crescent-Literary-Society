import os

# 1. Update about.html to replace emojis with SVGs
about_file = 'e:/CLS/about.html'
with open(about_file, 'r', encoding='utf-8') as f:
    about_html = f.read()

# Creative Expression
about_html = about_html.replace(
    '<div class="wwd-icon">✍️</div>',
    '<div class="wwd-icon"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 19l7-7 3 3-7 7-3-3z"></path><path d="M18 13l-1.5-7.5L2 2l3.5 14.5L13 18l5-5z"></path><path d="M2 2l7.58 7.58"></path><circle cx="11" cy="11" r="2"></circle></svg></div>'
)

# Public Speaking
about_html = about_html.replace(
    '<div class="wwd-icon">🎤</div>',
    '<div class="wwd-icon"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z"></path><path d="M19 10v2a7 7 0 0 1-14 0v-2"></path><line x1="12" y1="19" x2="12" y2="23"></line><line x1="8" y1="23" x2="16" y2="23"></line></svg></div>'
)

# Critical Thinking
about_html = about_html.replace(
    '<div class="wwd-icon">🧠</div>',
    '<div class="wwd-icon"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path></svg></div>'
)

# Lifelong Community
about_html = about_html.replace(
    '<div class="wwd-icon">🤝</div>',
    '<div class="wwd-icon"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg></div>'
)

with open(about_file, 'w', encoding='utf-8') as f:
    f.write(about_html)


# 2. Update footer.css to increase size and brightness
footer_css_file = 'e:/CLS/css/footer.css'
with open(footer_css_file, 'r', encoding='utf-8') as f:
    footer_css = f.read()

# .footer-tagline
footer_css = footer_css.replace(
'''.footer-tagline {
  font-family: var(--font-nav);
  font-size: 10px;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--accent-gold);
  margin-top: 0.15rem;
}''',
'''.footer-tagline {
  font-family: var(--font-nav);
  font-size: 12px;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: #d4af37;
  margin-top: 0.15rem;
}'''
)

# .footer-brand > p
footer_css = footer_css.replace(
'''.footer-brand > p {
  font-size: 0.9rem;
  line-height: 1.75;
  max-width: 290px;
  margin-bottom: 1.75rem;
}''',
'''.footer-brand > p {
  font-size: 0.95rem;
  line-height: 1.75;
  max-width: 290px;
  margin-bottom: 1.75rem;
  color: var(--text-primary);
}'''
)

# .footer-col-title
footer_css = footer_css.replace(
'''.footer-col-title {
  font-family: var(--font-nav);
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: var(--accent-gold);
  margin-bottom: 1.5rem;
  display: block;
}''',
'''.footer-col-title {
  font-family: var(--font-nav);
  font-size: 13px;
  font-weight: 700;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: #d4af37;
  margin-bottom: 1.5rem;
  display: block;
}'''
)

# .footer-nav-list a
footer_css = footer_css.replace(
'''.footer-nav-list a {
  font-family: var(--font-body);
  font-size: 0.9rem;
  color: var(--text-secondary);
  transition: color var(--transition), padding-left var(--transition);
}''',
'''.footer-nav-list a {
  font-family: var(--font-body);
  font-size: 0.98rem;
  color: var(--text-primary);
  transition: color var(--transition), padding-left var(--transition);
}'''
)

# .footer-contact-item a, .footer-contact-item span
footer_css = footer_css.replace(
'''.footer-contact-item a,
.footer-contact-item span {
  font-size: 0.88rem;
  color: var(--text-secondary);
  transition: color var(--transition);
  line-height: 1.4;
}''',
'''.footer-contact-item a,
.footer-contact-item span {
  font-size: 0.95rem;
  color: var(--text-primary);
  transition: color var(--transition);
  line-height: 1.4;
}'''
)

# .footer-motto
footer_css = footer_css.replace(
'''.footer-motto {
  font-family: var(--font-display);
  font-size: 1.15rem;
  color: var(--text-primary);
}''',
'''.footer-motto {
  font-family: var(--font-display);
  font-size: 1.25rem;
  color: var(--text-primary);
}'''
)

# .footer-istd
footer_css = footer_css.replace(
'''.footer-istd {
  font-size: 0.85rem;
  color: var(--text-secondary);
}''',
'''.footer-istd {
  font-size: 0.9rem;
  color: var(--text-primary);
}'''
)

# .footer-copyright
footer_css = footer_css.replace(
'''.footer-copyright {
  font-family: var(--font-nav);
  font-size: 13px;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--text-secondary);
}''',
'''.footer-copyright {
  font-family: var(--font-nav);
  font-size: 14px;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--text-primary);
}'''
)

with open(footer_css_file, 'w', encoding='utf-8') as f:
    f.write(footer_css)

print("done")

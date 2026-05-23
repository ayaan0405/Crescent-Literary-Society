import os
import glob

html_files = glob.glob("e:/CLS/*.html")

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Add script to head if not present
    if '<script src="js/theme.js"></script>' not in content:
        content = content.replace('</head>', '  <script src="js/theme.js"></script>\n</head>')

    # Add button to nav-menu if not present
    button_html = '<li class="nav-item-theme"><button id="theme-toggle" class="btn-ghost" style="padding: 0.4rem 0.8rem; margin-left: 1rem; cursor: pointer; border-radius: var(--radius); font-family: var(--font-display); background: transparent; color: var(--text-primary); border: 1px solid var(--border-card);">🌓 Theme</button></li>'
    if 'id="theme-toggle"' not in content:
        content = content.replace('</ul>\n      </nav>', f'  {button_html}\n      </ul>\n      </nav>')
        # Note: some files might have </ul>\n    </div> instead depending on structure.
        # Let's check a more robust replacement: finding the closing </ul> of the nav-menu
        import re
        content = re.sub(r'(<ul class="nav-menu"[^>]*>.*?)</ul>', r'\1  ' + button_html + r'\n      </ul>', content, flags=re.DOTALL)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Patched {len(html_files)} HTML files.")

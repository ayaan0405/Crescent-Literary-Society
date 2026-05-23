import glob
import re

html_files = glob.glob("e:/CLS/*.html")

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # The button currently has: color: var(--text-primary); border: 1px solid var(--border-card);
    # Let's just remove those specific inline styles.
    content = content.replace('color: var(--text-primary); border: 1px solid var(--border-card); ', '')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Removed inline colors from theme button.")

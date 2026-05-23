import os
import glob
from bs4 import BeautifulSoup

html_files = glob.glob("e:/CLS/*.html")

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        html_doc = f.read()

    soup = BeautifulSoup(html_doc, 'html.parser')
    
    # Check if script is in head
    head = soup.find('head')
    if head:
        scripts = head.find_all('script', src='js/theme.js')
        if not scripts:
            script_tag = soup.new_tag('script', src='js/theme.js')
            head.append(script_tag)
            
    # Check if button is in nav
    nav_menu = soup.find('ul', id='nav-menu')
    if nav_menu:
        # First remove any existing theme-toggle buttons (like the incorrectly placed one)
        existing_toggles = soup.find_all('li', class_='nav-item-theme')
        for toggle in existing_toggles:
            toggle.decompose()
            
        # Add the button as a direct child of nav-menu
        li_tag = soup.new_tag('li', attrs={'class': 'nav-item-theme', 'style': 'display: flex; align-items: center;'})
        button_tag = soup.new_tag('button', id='theme-toggle', attrs={
            'class': 'btn-ghost', 
            'style': 'padding: 0.4rem 0.8rem; margin-left: 1rem; cursor: pointer; border-radius: var(--radius); font-family: var(--font-display); background: transparent; color: var(--text-primary); border: 1px solid var(--border-card); display: flex; align-items: center; gap: 0.5rem;'
        })
        # Add an SVG icon and text
        button_tag.string = "Theme 🌓"
        li_tag.append(button_tag)
        nav_menu.append(li_tag)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(str(soup))

print(f"Patched {len(html_files)} HTML files using BeautifulSoup.")

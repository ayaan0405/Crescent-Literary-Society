import glob, re, os

# 1. Rename Miraki -> Meraki across all files
for file in glob.glob('e:/CLS/*.html') + glob.glob('e:/CLS/css/*.css'):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Case sensitive replacements
    new_content = content.replace('miraki.html', 'meraki.html')
    new_content = new_content.replace('Miraki', 'Meraki')
    
    if content != new_content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)

# Rename the file if it hasn't been renamed yet
if os.path.exists('e:/CLS/miraki.html'):
    os.rename('e:/CLS/miraki.html', 'e:/CLS/meraki.html')

print("Meraki renamed")

# 2. Fix global.css .card
with open('e:/CLS/css/global.css', 'r', encoding='utf-8') as f:
    g_content = f.read()
if "flex-direction: column;" not in g_content.split('.card {')[1].split('}')[0]:
    g_content = g_content.replace('.card {\n  background: var(--bg-card);\n  border: 1px solid var(--border-card);\n  border-radius: var(--radius);\n  overflow: hidden;\n  transition: transform var(--transition), box-shadow var(--transition);\n}',
                                  '.card {\n  background: var(--bg-card);\n  border: 1px solid var(--border-card);\n  border-radius: var(--radius);\n  overflow: hidden;\n  transition: transform var(--transition), box-shadow var(--transition);\n  display: flex;\n  flex-direction: column;\n}')
    with open('e:/CLS/css/global.css', 'w', encoding='utf-8') as f:
        f.write(g_content)
    print("Fixed global.css")

# 3. Fix nav.css theme toggle and logo bold
with open('e:/CLS/css/nav.css', 'r', encoding='utf-8') as f:
    n_content = f.read()
    
n_content = re.sub(
    r'\.nav-logo-sub\s*\{[^}]*\}',
    '.nav-logo-sub {\n  font-family: var(--font-nav);\n  font-size: 11px;\n  font-weight: 600;\n  letter-spacing: 0.28em;\n  text-transform: uppercase;\n  color: var(--text-secondary);\n}',
    n_content
)

n_content = n_content.replace(
'''#theme-toggle {
  color: var(--text-primary) !important;
  border: 1px solid var(--border-card) !important;
}

#theme-toggle:hover {
  background: var(--bg-secondary) !important;
}''',
'''#theme-toggle {
  color: var(--text-primary) !important;
  border: none !important;
  border-radius: 50px !important;
  background: rgba(128,128,128,0.1) !important;
}

#theme-toggle:hover {
  background: rgba(128,128,128,0.2) !important;
}'''
)

n_content = n_content.replace(
'''#theme-toggle {
  color: #ffffff;
  border: 1px solid rgba(255, 255, 255, 0.25);
  transition: all var(--transition);
}''',
'''#theme-toggle {
  color: var(--text-primary);
  border: none;
  background: rgba(128,128,128,0.15);
  border-radius: 50px;
  transition: all var(--transition);
}'''
)

with open('e:/CLS/css/nav.css', 'w', encoding='utf-8') as f:
    f.write(n_content)
print("Fixed nav.css")

# 4. Fix pages.css .about-lead and .about-fw-sub
with open('e:/CLS/css/pages.css', 'r', encoding='utf-8') as f:
    p_content = f.read()

p_content = p_content.replace('color: rgba(255,255,255,0.9);', 'color: var(--text-primary);')
p_content = p_content.replace('color: rgba(255,255,255,0.7);', 'color: var(--text-secondary);')

with open('e:/CLS/css/pages.css', 'w', encoding='utf-8') as f:
    f.write(p_content)
print("Fixed pages.css")


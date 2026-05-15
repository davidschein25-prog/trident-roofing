import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Remove the logo-showcase-card and exp-badge-premium, keeping just the logo
# The pattern needs to match the existing structure precisely
pattern = r'<div class="about-visual reveal" style="transition-delay: 0.2s;">\s*<div class="logo-showcase-card">.*?<img src="assets/logo.png" alt="Trident Roofing Logo" class="about-logo">.*?<div class="exp-badge-premium".*?</div>\s*</div>\s*</div>'

new_visual_html = """
                <div class="about-visual reveal" style="transition-delay: 0.2s; display: flex; justify-content: center; align-items: center;">
                    <img src="assets/logo.png" alt="Trident Roofing Logo" class="about-logo" style="max-width: 280px; filter: drop-shadow(0 15px 30px rgba(0,0,0,0.1));">
                </div>"""

# Apply replacement
html = re.sub(pattern, new_visual_html, html, flags=re.DOTALL)

# 2. Reduce margin-top on reviews-marquee
html = html.replace('style="margin-top: 4rem;"', 'style="margin-top: 1rem;"')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated index.html")

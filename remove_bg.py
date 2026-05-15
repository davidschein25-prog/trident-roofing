import os
import re

css_path = "c:\\Users\\Admin\\Documents\\dev stuff\\Roofing\\css\\style.css"
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

old_css = """.reviews-marquee {
    background: var(--secondary-bg);
    padding: 3rem 0;
    overflow: hidden;
    position: relative;
    border-top: 1px solid var(--glass-border);
    border-bottom: 1px solid var(--glass-border);
}"""

new_css = """.reviews-marquee {
    background: transparent;
    padding: 3rem 0;
    overflow: hidden;
    position: relative;
}"""

css = css.replace(old_css, new_css)

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css)

# Cache bust index.html
index_path = "c:\\Users\\Admin\\Documents\\dev stuff\\Roofing\\index.html"
with open(index_path, "r", encoding="utf-8") as f:
    html = f.read()

html = re.sub(r'js/app\.js\?v=\d+', 'js/app.js?v=43', html)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Done")

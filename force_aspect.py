import os
import re

css_path = "c:\\Users\\Admin\\Documents\\dev stuff\\Roofing\\css\\style.css"
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

old_css = """.blueprint-img {
    width: 100%;
    height: auto;"""
new_css = """.blueprint-img {
    width: 100%;
    height: auto;
    aspect-ratio: 1 / 1;
    object-fit: cover;
    object-position: center;"""

css = css.replace(old_css, new_css)

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css)

# Cache bust index.html
index_path = "c:\\Users\\Admin\\Documents\\dev stuff\\Roofing\\index.html"
with open(index_path, "r", encoding="utf-8") as f:
    html = f.read()

html = re.sub(r'js/app\.js\?v=\d+', 'js/app.js?v=46', html)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Done")

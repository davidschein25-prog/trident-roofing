import os
import re

css_path = "c:\\Users\\Admin\\Documents\\dev stuff\\Roofing\\css\\style.css"
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

# Fix PC padding
css = css.replace("padding: 1.5rem;", "padding: 0 1.5rem;")

# Fix mobile padding
css = css.replace("padding: 0.5rem;", "padding: 0 0.5rem;")

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css)

# --- 4. Update index.html cache bust ---
index_path = "c:\\Users\\Admin\\Documents\\dev stuff\\Roofing\\index.html"
with open(index_path, "r", encoding="utf-8") as f:
    html = f.read()

html = re.sub(r'js/app\.js\?v=\d+', 'js/app.js?v=37', html)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Done")

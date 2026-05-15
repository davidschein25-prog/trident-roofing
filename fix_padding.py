import os
import re

css_path = "c:\\Users\\Admin\\Documents\\dev stuff\\Roofing\\css\\style.css"
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

css = css.replace(".service-modal { padding: 0 1.5rem; max-height: 95vh; }", ".service-modal { padding: 2rem 1.5rem; max-height: 95vh; }")

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css)

# Cache bust index.html
index_path = "c:\\Users\\Admin\\Documents\\dev stuff\\Roofing\\index.html"
with open(index_path, "r", encoding="utf-8") as f:
    html = f.read()

html = re.sub(r'js/app\.js\?v=\d+', 'js/app.js?v=44', html)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Done")

import os
import re

css_path = "c:\\Users\\Admin\\Documents\\dev stuff\\Roofing\\css\\style.css"
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

# Remove the 2:1 aspect ratio constraint
css = css.replace("    aspect-ratio: 2 / 1; /* Forces the container to be wide and short, cutting vertical height in half */\n", "")

# Restore normal image sizing
old_img_css = """    height: 100%;
    object-fit: cover;
    object-position: center;"""
new_img_css = "    height: auto;"
css = css.replace(old_img_css, new_img_css)

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css)

# Cache bust index.html
index_path = "c:\\Users\\Admin\\Documents\\dev stuff\\Roofing\\index.html"
with open(index_path, "r", encoding="utf-8") as f:
    html = f.read()

html = re.sub(r'js/app\.js\?v=\d+', 'js/app.js?v=45', html)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Done")

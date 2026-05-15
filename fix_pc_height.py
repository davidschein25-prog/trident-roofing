import os
import re

css_path = "c:\\Users\\Admin\\Documents\\dev stuff\\Roofing\\css\\style.css"
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

old_css = """@media (min-width: 992px) {
    .engineering-standard {
        display: grid;
        grid-template-columns: 1fr 2fr;
        gap: 3rem;
        align-items: center;
        padding: 3rem;
    }
    .standard-header h3, .standard-header p {
        text-align: left;
    }
}"""

new_css = """@media (min-width: 992px) {
    .engineering-standard {
        display: grid;
        grid-template-columns: 1fr 1fr; /* 50/50 split gives the image less width, making its 1:1 height much smaller */
        gap: 4rem;
        align-items: center;
        padding: 3rem;
    }
    .standard-header h3, .standard-header p {
        text-align: left;
    }
    .blueprint-outer {
        max-width: 500px; /* Constrain specifically on PC to prevent it from getting too tall */
        margin-left: auto; /* Push it towards the right side of its grid column */
        margin-right: 0;
    }
}"""

css = css.replace(old_css, new_css)

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css)

# Cache bust index.html
index_path = "c:\\Users\\Admin\\Documents\\dev stuff\\Roofing\\index.html"
with open(index_path, "r", encoding="utf-8") as f:
    html = f.read()

html = re.sub(r'js/app\.js\?v=\d+', 'js/app.js?v=47', html)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Done")

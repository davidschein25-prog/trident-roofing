import os
import re

# 1. Update index.html
index_path = "c:\\Users\\Admin\\Documents\\dev stuff\\Roofing\\index.html"
with open(index_path, "r", encoding="utf-8") as f:
    html = f.read()

old_html = """                        <p class="text-dim mb-md">Precision layers designed for the Ontario climate.</p>
                        <p class="text-dim mb-lg" style="font-size: 1.05rem; line-height: 1.6;">The diagram highlights the core structural components of a Trident engineered installation. <strong>Hover over or tap</strong> the pulsing markers to explore the premium materials and precise techniques we use to protect your home from the elements.</p>"""

new_html = """                        <p class="text-dim mb-lg" style="font-size: 1.05rem; line-height: 1.6;">The diagram highlights the core structural components of a Trident engineered installation. <strong>Hover over or tap</strong> the pulsing markers to explore the premium materials and precise techniques we use to protect your home from the elements. Precision layers designed for the Ontario climate.</p>"""

html = html.replace(old_html, new_html)

# Cache bust
html = re.sub(r'js/app\.js\?v=\d+', 'js/app.js?v=50', html)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(html)


# 2. Update style.css
css_path = "c:\\Users\\Admin\\Documents\\dev stuff\\Roofing\\css\\style.css"
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

old_css = """    .standard-header h3, .standard-header p {
        text-align: left;
    }"""

new_css = """    .standard-header h3, .standard-header p {
        text-align: left;
    }
    .standard-header h3 {
        font-size: 2.5rem; /* Increase font size specifically for PC view */
        line-height: 1.2;
        margin-bottom: 1.5rem;
    }"""

css = css.replace(old_css, new_css)

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css)

print("Done")

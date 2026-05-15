import os
import re

# 1. Update index.html
index_path = "c:\\Users\\Admin\\Documents\\dev stuff\\Roofing\\index.html"
with open(index_path, "r", encoding="utf-8") as f:
    html = f.read()

# Remove text-center class from standard header items
html = html.replace('<h3 class="text-center">The Trident Engineering Standard</h3>', '<h3>The Trident Engineering Standard</h3>')
html = html.replace('<p class="text-center text-dim mb-lg">Precision layers designed for the Ontario climate.</p>', '<p class="text-dim mb-lg">Precision layers designed for the Ontario climate.</p>')

# Cache bust
html = re.sub(r'js/app\.js\?v=\d+', 'js/app.js?v=40', html)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(html)


# 2. Update style.css
css_path = "c:\\Users\\Admin\\Documents\\dev stuff\\Roofing\\css\\style.css"
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

# Replace .engineering-standard section with responsive grid styles
new_css = """/* Engineering Standard / Blueprint Section */
.engineering-standard {
    background: rgba(107, 142, 155, 0.03);
    border-radius: var(--radius-lg);
    padding: 2rem 1.5rem;
    margin-top: 2rem;
    border: 1px solid rgba(181, 207, 216, 0.1);
}

.standard-header h3, .standard-header p {
    text-align: center;
}

@media (min-width: 992px) {
    .engineering-standard {
        display: grid;
        grid-template-columns: 1fr 2.5fr;
        gap: 3rem;
        align-items: center;
        padding: 3rem;
    }
    .standard-header h3, .standard-header p {
        text-align: left;
    }
}
"""

css = re.sub(r'/\* Engineering Standard / Blueprint Section \*/.*?(?=\.standard-header h3 {)', new_css, css, flags=re.DOTALL)

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css)

# Update contact html cache
contact_path = "c:\\Users\\Admin\\Documents\\dev stuff\\Roofing\\contact.html"
with open(contact_path, "r", encoding="utf-8") as f:
    contact_html = f.read()

contact_html = re.sub(r'js/app\.js\?v=\d+', 'js/app.js?v=40', contact_html)

with open(contact_path, "w", encoding="utf-8") as f:
    f.write(contact_html)

print("Layout updated.")

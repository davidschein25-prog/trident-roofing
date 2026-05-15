import os
import re

# --- 1. Update CSS ---
css_path = "c:\\Users\\Admin\\Documents\\dev stuff\\Roofing\\css\\style.css"
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

# Add padding to image-box
css = css.replace("padding: 0 0.75rem;", "padding: 1.5rem;")

# Remove 1fr on mobile for services-grid so it stays 2 columns
old_mobile_grid = """@media (max-width: 768px) {
    .services-grid {
        grid-template-columns: 1fr;
    }
}"""
new_mobile_grid = """@media (max-width: 768px) {
    .services-grid {
        grid-template-columns: repeat(2, 1fr);
        gap: 1rem;
    }
    .service-card-premium .image-box {
        height: 150px; /* smaller height for mobile 2 column */
        padding: 0.5rem;
    }
    .service-card-premium h3 {
        font-size: 1.1rem;
    }
    .service-card-premium p {
        font-size: 0.8rem;
    }
}"""
if old_mobile_grid in css:
    css = css.replace(old_mobile_grid, new_mobile_grid)
else:
    css += new_mobile_grid

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css)

# --- 2. Update index.html ---
index_path = "c:\\Users\\Admin\\Documents\\dev stuff\\Roofing\\index.html"
with open(index_path, "r", encoding="utf-8") as f:
    html = f.read()

# Fix storm response button
html = html.replace('Get Immediate Help <i class="fas fa-arrow-right"></i>', 'Explore System <i class="fas fa-arrow-right"></i>')

# Add scroll indicator
# We'll inject it just before the closing tag of .hero-sticky
old_hero_close = "            </div>\n        </section>\n\n        <!-- Why Trident Comparison -->"
new_hero_close = """                <!-- Scroll Indicator -->
                <div class="scroll-indicator">
                    <span class="scroll-text">Scroll to learn more</span>
                    <i class="fas fa-chevron-down"></i>
                </div>
            </div>
        </section>

        <!-- Why Trident Comparison -->"""

if '<div class="scroll-indicator">' not in html:
    html = html.replace(old_hero_close, new_hero_close)

# Bust cache
html = re.sub(r'js/app\.js\?v=\d+', 'js/app.js?v=36', html)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Done")

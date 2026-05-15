import os
import shutil
import re

# --- 1. Copy Images ---
assets_dir = "c:\\Users\\Admin\\Documents\\dev stuff\\Roofing\\assets\\"
dark_house = "C:\\Users\\Admin\\.gemini\\antigravity\\brain\\ef15b4ff-7230-4030-946c-e7b81ca1dc16\\vector_house_dark_1778738665853.png"
skylight = "C:\\Users\\Admin\\.gemini\\antigravity\\brain\\ef15b4ff-7230-4030-946c-e7b81ca1dc16\\service_skylight_1778738692182.png"
emergency = "C:\\Users\\Admin\\.gemini\\antigravity\\brain\\ef15b4ff-7230-4030-946c-e7b81ca1dc16\\service_emergency_1778738707959.png"

shutil.copy(dark_house, os.path.join(assets_dir, "vector_house.png"))
shutil.copy(skylight, os.path.join(assets_dir, "service_skylight.png"))
shutil.copy(emergency, os.path.join(assets_dir, "service_emergency.png"))

# --- 2. Update CSS ---
css_path = "c:\\Users\\Admin\\Documents\\dev stuff\\Roofing\\css\\style.css"
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

# Fix custom dropdown content label
old_label_css = ".custom-dropdown-content label {"
new_label_css = """
.custom-dropdown-content label {
    display: flex !important;
    align-items: center !important;
    justify-content: flex-start !important;
    gap: 10px !important;
    padding: 0.5rem !important;
    margin: 0 !important;
    width: 100% !important;
    white-space: nowrap !important;
}
.custom-dropdown-content input[type="checkbox"] {
    width: auto !important;
    margin: 0 !important;
    transform: scale(1.2);
}
/* temporary marker */
.custom-dropdown-content-label-old {"""

css = css.replace(old_label_css, new_label_css)

# Pause marquee on hover
if "animation-play-state: paused" not in css:
    css += """
.reviews-marquee:hover .marquee-content,
.reviews-marquee:active .marquee-content {
    animation-play-state: paused;
}
"""

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css)

# --- 3. Update index.html ---
index_path = "c:\\Users\\Admin\\Documents\\dev stuff\\Roofing\\index.html"
with open(index_path, "r", encoding="utf-8") as f:
    html = f.read()

# Replace skylights image
html = html.replace('src="assets/service_gutter_guard_new.png" alt="Skylights and Sun Tunnels"', 'src="assets/service_skylight.png" alt="Skylights and Sun Tunnels"')

# Replace emergency card
old_emergency = """                    <!-- Storm & Leak Response — spans full width -->
                    <div class="service-card-premium service-card-emergency reveal service-modal-trigger" data-service="emergency" style="transition-delay: 0.4s; cursor: pointer;">
                        <div class="emergency-banner">
                            <div class="emergency-icon">
                                <i class="fas fa-bolt"></i>
                            </div>
                            <div class="emergency-content">
                                <h3>Storm Response & Insurance Claims</h3>
                                <p>Active leak or storm damage? We provide 24/7 emergency mitigation and full insurance claim assistance to ensure you are covered.</p>
                            </div>
                            <div class="emergency-actions" style="display: flex; gap: 1rem; align-items: center; flex-wrap: wrap;">
                                <a href="tel:2266800996" class="btn btn-primary"><i class="fas fa-phone-alt"></i> Call Now</a>
                                <button class="btn btn-secondary">Claim Details <i class="fas fa-arrow-right"></i></button>
                            </div>
                        </div>
                    </div>"""

new_emergency = """                    <div class="service-card-premium reveal service-modal-trigger" data-service="emergency" style="cursor: pointer;">
                        <div class="image-box">
                            <img src="assets/service_emergency.png" alt="Emergency Storm Response">
                        </div>
                        <div class="content-box">
                            <h3 style="color: var(--accent-red);"><i class="fas fa-bolt"></i> Storm Response</h3>
                            <p>Active leak or storm damage? We provide 24/7 emergency mitigation and full insurance claim assistance.</p>
                            <button class="nav-link" style="color: var(--accent-red);">Get Immediate Help <i class="fas fa-arrow-right"></i></button>
                        </div>
                    </div>"""

html = html.replace(old_emergency, new_emergency)

# Bust cache
html = re.sub(r'js/app\.js\?v=\d+', 'js/app.js?v=35', html)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(html)

# --- 4. Update contact.html cache bust ---
contact_path = "c:\\Users\\Admin\\Documents\\dev stuff\\Roofing\\contact.html"
with open(contact_path, "r", encoding="utf-8") as f:
    contact_html = f.read()

contact_html = re.sub(r'js/app\.js\?v=\d+', 'js/app.js?v=35', contact_html)

with open(contact_path, "w", encoding="utf-8") as f:
    f.write(contact_html)

print("Done")

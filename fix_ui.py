import os

# --- 1. Update CSS ---
css_path = "c:\\Users\\Admin\\Documents\\dev stuff\\Roofing\\css\\style.css"
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

# Change services grid from 4 to 3 columns
css = css.replace("grid-template-columns: repeat(4, 1fr);", "grid-template-columns: repeat(3, 1fr);")

# Add mobile grid layout and custom dropdown CSS
if ".custom-dropdown" not in css:
    css += """
@media (max-width: 1024px) {
    .services-grid {
        grid-template-columns: repeat(2, 1fr);
    }
}
@media (max-width: 768px) {
    .services-grid {
        grid-template-columns: 1fr;
    }
}

/* Custom Dropdown for Contact Form */
.custom-dropdown {
    position: relative;
    width: 100%;
}
.custom-dropdown-header {
    background: var(--white);
    border: 1px solid var(--glass-border);
    padding: 1rem;
    border-radius: var(--radius-sm);
    color: var(--text-main);
    cursor: pointer;
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.custom-dropdown-content {
    position: absolute;
    top: 100%;
    left: 0;
    right: 0;
    background: var(--white);
    border: 1px solid var(--accent-blue);
    border-radius: var(--radius-sm);
    padding: 1rem;
    z-index: 100;
    display: none;
    flex-direction: column;
    gap: 0.5rem;
    box-shadow: var(--shadow-heavy);
}
.custom-dropdown-content.open {
    display: flex;
}
.custom-dropdown-content label {
    display: flex;
    align-items: center;
    gap: 10px;
    cursor: pointer;
    font-size: 0.95rem;
    color: var(--text-main);
    margin-bottom: 0;
}
"""
with open(css_path, "w", encoding="utf-8") as f:
    f.write(css)

# --- 2. Update contact.html ---
contact_path = "c:\\Users\\Admin\\Documents\\dev stuff\\Roofing\\contact.html"
with open(contact_path, "r", encoding="utf-8") as f:
    contact_html = f.read()

old_select = """                            <div class="form-group">
                                <label for="service-type">Interested System(s)</label>
                                <select id="service-type" name="service-type" multiple style="height: 120px; color: var(--accent-blue);">
                                    <option value="roofing">Roofing System</option>
                                    <option value="siding">Siding System</option>
                                    <option value="eavestroughs">Eavestroughs & Gutter Guards</option>
                                    <option value="skylights">Skylights & Sun Tunnels</option>
                                    <option value="specialty">Custom Exterior Solutions</option>
                                    <option value="emergency">Emergency Response</option>
                                </select>
                                <small style="color: var(--text-dim);">Hold Ctrl (or Cmd) to select multiple</small>
                            </div>"""

new_select = """                            <div class="form-group">
                                <label>Interested System(s)</label>
                                <div class="custom-dropdown" id="custom-dropdown">
                                    <div class="custom-dropdown-header" id="custom-dropdown-header">Select Interested System(s) <i class="fas fa-chevron-down"></i></div>
                                    <div class="custom-dropdown-content" id="custom-dropdown-content">
                                        <label><input type="checkbox" name="services" value="roofing"> Roofing System</label>
                                        <label><input type="checkbox" name="services" value="siding"> Siding System</label>
                                        <label><input type="checkbox" name="services" value="eavestroughs"> Eavestroughs & Gutter Guards</label>
                                        <label><input type="checkbox" name="services" value="skylights"> Skylights & Sun Tunnels</label>
                                        <label><input type="checkbox" name="services" value="specialty"> Custom Exterior Solutions</label>
                                        <label><input type="checkbox" name="services" value="emergency"> Emergency Response</label>
                                        <button type="button" class="btn btn-primary btn-sm" id="dropdown-confirm-btn" style="margin-top:10px; width:100%; justify-content: center;">Confirm</button>
                                    </div>
                                </div>
                            </div>"""

contact_html = contact_html.replace(old_select, new_select)
with open(contact_path, "w", encoding="utf-8") as f:
    f.write(contact_html)

# --- 3. Update app.js ---
app_path = "c:\\Users\\Admin\\Documents\\dev stuff\\Roofing\\js\\app.js"
with open(app_path, "r", encoding="utf-8") as f:
    app_js = f.read()

# Replace Trident Edge logic to use modal instead of alert
old_trident = """function initTridentEdge() {
    const items = document.querySelectorAll('.clickable-edge');
    items.forEach(item => {
        item.addEventListener('click', () => {
            const detail = item.getAttribute('data-detail');
            if(detail) {
                alert(detail); // Simple alert for now, could be a tooltip or modal
            }
        });
    });
}"""

new_trident = """function initTridentEdge() {
    const items = document.querySelectorAll('.clickable-edge');
    const modal = document.getElementById('service-modal');
    const modalBody = document.getElementById('modal-body');
    
    items.forEach(item => {
        item.addEventListener('click', () => {
            const detail = item.getAttribute('data-detail');
            const title = item.querySelector('span').innerText;
            if(detail && modalBody && modal) {
                modalBody.innerHTML = `
                    <div class="modal-subtitle" style="color: var(--accent-orange); font-weight: 600; margin-bottom: 0.5rem;">The Trident Edge</div>
                    <h2 style="margin-bottom: 1rem;">${title}</h2>
                    <p style="margin-bottom: 2rem;">${detail}</p>
                    <button class="btn btn-primary modal-cta" onclick="document.getElementById('service-modal').classList.remove('active'); document.body.style.overflow = '';">Got it <i class="fas fa-check"></i></button>
                `;
                modal.classList.add('active');
                document.body.style.overflow = 'hidden';
            }
        });
    });
}"""
app_js = app_js.replace(old_trident, new_trident)

# Add initCustomDropdown() to DOMContentLoaded
app_js = app_js.replace("initTridentEdge();\n", "initTridentEdge();\n    initCustomDropdown();\n")

custom_dropdown_js = """
/**
 * Custom Dropdown Logic
 */
function initCustomDropdown() {
    const header = document.getElementById('custom-dropdown-header');
    const content = document.getElementById('custom-dropdown-content');
    const confirmBtn = document.getElementById('dropdown-confirm-btn');
    const checkboxes = document.querySelectorAll('.custom-dropdown-content input[type="checkbox"]');
    
    if (!header || !content || !confirmBtn) return;
    
    header.addEventListener('click', () => {
        content.classList.toggle('open');
    });
    
    const updateHeader = () => {
        const checked = Array.from(checkboxes).filter(cb => cb.checked).map(cb => cb.parentElement.innerText.trim());
        if (checked.length === 0) {
            header.innerHTML = 'Select Interested System(s) <i class="fas fa-chevron-down"></i>';
        } else if (checked.length === 1) {
            header.innerHTML = checked[0] + ' <i class="fas fa-chevron-down"></i>';
        } else {
            header.innerHTML = checked.length + ' Systems Selected <i class="fas fa-chevron-down"></i>';
        }
    };
    
    checkboxes.forEach(cb => {
        cb.addEventListener('change', updateHeader);
    });
    
    confirmBtn.addEventListener('click', () => {
        content.classList.remove('open');
    });
}
"""

app_js += custom_dropdown_js

# update form handler array extraction
old_extract = """        const select = form.querySelector('#service-type');
        if (select) {
            data.services = Array.from(select.selectedOptions).map(opt => opt.value);
        }"""
new_extract = """        const checkboxes = form.querySelectorAll('.custom-dropdown-content input[type="checkbox"]:checked');
        if (checkboxes.length > 0) {
            data.services = Array.from(checkboxes).map(cb => cb.value);
        }"""
app_js = app_js.replace(old_extract, new_extract)

with open(app_path, "w", encoding="utf-8") as f:
    f.write(app_js)


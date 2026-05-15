import os
import re

js_path = "c:\\Users\\Admin\\Documents\\dev stuff\\Roofing\\js\\app.js"
with open(js_path, "r", encoding="utf-8") as f:
    js = f.read()

# Add initBlueprintHotspots(); to DOMContentLoaded
old_init = """    initTridentEdge();
    initCustomDropdown();
    initMagneticButtons();
});"""
new_init = """    initTridentEdge();
    initCustomDropdown();
    initMagneticButtons();
    initBlueprintHotspots();
});"""

js = js.replace(old_init, new_init)

# Append the function
blueprint_func = """

function initBlueprintHotspots() {
    const items = document.querySelectorAll('.clickable-hotspot');
    const modal = document.getElementById('service-modal');
    const modalBody = document.getElementById('modal-body');
    
    items.forEach(item => {
        item.addEventListener('click', () => {
            const detail = item.getAttribute('data-detail');
            const title = item.getAttribute('data-title');
            if(detail && modalBody && modal) {
                modalBody.innerHTML = `
                    <div class="modal-subtitle" style="color: var(--accent-orange); font-weight: 600; margin-bottom: 0.5rem;">Trident Engineering Standard</div>
                    <h2 style="margin-bottom: 1rem;">${title}</h2>
                    <p style="margin-bottom: 2rem;">${detail}</p>
                    <button class="btn btn-primary modal-cta" onclick="document.getElementById('service-modal').classList.remove('active'); document.body.style.overflow = '';">Got it <i class="fas fa-check"></i></button>
                `;
                modal.classList.add('active');
                document.body.style.overflow = 'hidden';
            }
        });
    });
}
"""

js += blueprint_func

with open(js_path, "w", encoding="utf-8") as f:
    f.write(js)

print("Updated app.js")

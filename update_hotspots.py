import os
import re

index_path = "c:\\Users\\Admin\\Documents\\dev stuff\\Roofing\\index.html"
with open(index_path, "r", encoding="utf-8") as f:
    html = f.read()

# Refactor the 5 hotspots
hotspots_data = [
    ("10%", "50%", "Premium Ridge Ventilation", "We use top-tier continuous airflow vents installed with precise measurements to permanently prevent attic heat buildup and deck rot."),
    ("25%", "30%", "Premium Shingle Systems", "Architectural shingles installed exclusively with 6-nail patterns and precise edge alignment for ultimate wind protection and longevity."),
    ("45%", "80%", "Seamless Eavestroughs", "Custom-formed seamless aluminum with Alu-Rex guard systems, perfectly pitched for high-capacity flow."),
    ("65%", "20%", "Architectural Siding", "Premium Westlake Royal siding with specialized house wrap and meticulously hand-cut corner mitres."),
    ("35%", "65%", "Maximum Protection Shield", "High-performance synthetic underlayment and double-layered ice & water shield in critical valleys.")
]

for top, left, title, detail in hotspots_data:
    # Regex to find the hotspot block
    # It looks like:
    # <div class="hotspot" style="top: 10%; left: 50%;">
    #     <div class="hotspot-pulse"></div>
    #     <div class="hotspot-label">
    #         <h4>Premium Ridge Ventilation</h4>
    #         <p>We use top-tier continuous airflow vents installed with precise measurements to permanently prevent attic heat buildup and deck rot.</p>
    #     </div>
    # </div>
    
    pattern = r'<div class="hotspot" style="top: ' + top + r'; left: ' + left + r';">.*?</div>\s*</div>'
    replacement = f'<div class="hotspot clickable-hotspot" style="top: {top}; left: {left}; cursor: pointer;" data-title="{title}" data-detail="{detail}">\n                                <div class="hotspot-pulse"></div>\n                            </div>'
    
    html = re.sub(pattern, replacement, html, flags=re.DOTALL)

# Cache bust
html = re.sub(r'js/app\.js\?v=\d+', 'js/app.js?v=48', html)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Updated index.html")

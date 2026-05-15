import os
import re

index_path = "c:\\Users\\Admin\\Documents\\dev stuff\\Roofing\\index.html"
with open(index_path, "r", encoding="utf-8") as f:
    html = f.read()

# Locate the carousel
start_marker = "        <!-- Floating Review Carousel -->"
end_marker = "        <!-- Section Moved Below -->"

start_idx = html.find(start_marker)
end_idx = html.find(end_marker)

if start_idx != -1 and end_idx != -1:
    carousel_html = html[start_idx:end_idx].strip()
    
    # Remove from original location
    html = html[:start_idx] + html[end_idx:]
    
    # Locate end of About section
    about_end_marker = "            </div>\n        </section>\n\n\n        <!-- Why Trident Comparison -->"
    
    # Actually, it's easier to just find the </section> of the about block.
    # Let's find "<!-- Why Trident Comparison -->" and insert before its preceding </section>
    why_trident_idx = html.find("        <!-- Why Trident Comparison -->")
    
    if why_trident_idx != -1:
        # Find the </section> just before it
        section_end_idx = html.rfind("</section>", 0, why_trident_idx)
        
        if section_end_idx != -1:
            # Insert the carousel before the </section>
            html = html[:section_end_idx] + "\n            " + carousel_html + "\n        " + html[section_end_idx:]
            
            # Add a bit of top margin to the carousel so it's not flush against the about content
            html = html.replace('class="reviews-marquee"', 'class="reviews-marquee" style="margin-top: 4rem;"')
            
            # Cache bust
            html = re.sub(r'js/app\.js\?v=\d+', 'js/app.js?v=42', html)
            
            with open(index_path, "w", encoding="utf-8") as f:
                f.write(html)
            print("Successfully moved the carousel.")
        else:
            print("Could not find </section>")
    else:
        print("Could not find Why Trident section")
else:
    print("Could not find carousel boundaries")

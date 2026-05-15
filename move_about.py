import os
import re

index_path = "c:\\Users\\Admin\\Documents\\dev stuff\\Roofing\\index.html"
with open(index_path, "r", encoding="utf-8") as f:
    html = f.read()

# Define the exact start and end of the About section
about_start = "        <!-- About Us Section -->"
about_end = "        </section>\n\n        <!-- Service Grid -->"

# Find the indices
start_idx = html.find(about_start)
end_idx = html.find("        <!-- Service Grid -->")

if start_idx != -1 and end_idx != -1:
    about_html = html[start_idx:end_idx]
    
    # Remove it from current position
    html = html[:start_idx] + html[end_idx:]
    
    # Define where to insert (before Why Trident)
    insert_marker = "        <!-- Why Trident Comparison -->"
    insert_idx = html.find(insert_marker)
    
    if insert_idx != -1:
        # Insert
        html = html[:insert_idx] + about_html + "\n" + html[insert_idx:]
        
        # Cache bust
        html = re.sub(r'js/app\.js\?v=\d+', 'js/app.js?v=41', html)
        
        with open(index_path, "w", encoding="utf-8") as f:
            f.write(html)
        print("Moved successfully")
    else:
        print("Could not find insert marker")
else:
    print("Could not find about section")

import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Pattern for the scroll indicator block
indicator_pattern = r'\s*<div class="scroll-indicator">.*?</div>'

# Find all matches
matches = list(re.finditer(indicator_pattern, html, flags=re.DOTALL))

if len(matches) > 1:
    # Keep the first one, remove the others
    # We iterate backwards to not mess up indices
    for m in reversed(matches[1:]):
        html = html[:m.start()] + html[m.end():]
    print(f"Removed {len(matches) - 1} duplicate indicators")
else:
    print("No duplicates found")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

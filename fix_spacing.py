with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove mb-sm from clickable-edge items
html = html.replace('class="mb-sm clickable-edge"', 'class="clickable-edge"')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated index.html")

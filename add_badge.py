with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the text with the badge div
old_text = '<p class="text-sm text-center mt-sm" style="color: var(--text-dim);"><em>* Click an item to learn more</em></p>'
new_badge = '<div class="click-badge"><i class="fas fa-mouse-pointer"></i> Click to learn more</div>'

html = html.replace(old_text, new_badge)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated index.html")

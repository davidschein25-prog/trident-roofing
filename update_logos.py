with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace text with images
html = html.replace('<div class="trust-item"><i class="fas fa-shield-alt"></i> IKO Approved</div>', '<div class="trust-item"><img src="assets/logo_iko.png" alt="IKO" class="trust-logo"></div>')
html = html.replace('<div class="trust-item"><i class="fas fa-check-double"></i> Westlake Royal</div>', '<div class="trust-item"><img src="assets/logo_westlake.png" alt="Westlake Royal" class="trust-logo"></div>')
html = html.replace('<div class="trust-item"><i class="fas fa-tools"></i> Velux Specialist</div>', '<div class="trust-item"><img src="assets/logo_velux.png" alt="Velux" class="trust-logo"></div>')
html = html.replace('<div class="trust-item"><i class="fas fa-tint"></i> Alu-Rex Preferred</div>', '<div class="trust-item"><img src="assets/logo_alurex.png" alt="Alu-Rex" class="trust-logo"></div>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated index.html")

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Restore text alongside logos
html = html.replace('<div class="trust-item"><img src="assets/logo_iko.png" alt="IKO" class="trust-logo"></div>', '<div class="trust-item"><img src="assets/logo_iko.png" alt="IKO" class="trust-logo"> IKO Approved</div>')
html = html.replace('<div class="trust-item"><img src="assets/logo_westlake.png" alt="Westlake Royal" class="trust-logo"></div>', '<div class="trust-item"><img src="assets/logo_westlake.png" alt="Westlake Royal" class="trust-logo"> Westlake Royal</div>')
html = html.replace('<div class="trust-item"><img src="assets/logo_velux.png" alt="Velux" class="trust-logo"></div>', '<div class="trust-item"><img src="assets/logo_velux.png" alt="Velux" class="trust-logo"> Velux Specialist</div>')
html = html.replace('<div class="trust-item"><img src="assets/logo_alurex.png" alt="Alu-Rex" class="trust-logo"></div>', '<div class="trust-item"><img src="assets/logo_alurex.png" alt="Alu-Rex" class="trust-logo"> Alu-Rex Preferred</div>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated index.html")

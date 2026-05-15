import re

with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Clean up ALL previous messy overrides for these sections
# I'll remove the blocks I added at the end of the file or that have messy comments
css = re.sub(r'/\* Restore Portfolio Size Overrides \*/.*?}\s*}', '', css, flags=re.DOTALL)
css = re.sub(r'/\* Kinetic Scroll indicator logic \*/.*?}\s*}', '', css, flags=re.DOTALL) # In case this exists

# 2. Explicitly set .about-grid PC layout (75/25)
# Find the rule and update it
css = re.sub(r'\.about-grid\s*{\s*display:\s*grid;\s*grid-template-columns:\s*[^;]+;\s*gap:\s*[^;]+;\s*align-items:\s*center;\s*}', 
             '.about-grid {\n    display: grid;\n    grid-template-columns: 1.5fr 0.5fr; /* 75/25 split */\n    gap: 3rem;\n    align-items: center;\n}', 
             css)

# 3. Explicitly set .engineering-standard PC layout (50/50)
# Find the rule inside @media (min-width: 992px)
# I'll use a more surgical replacement for the block inside the media query
pattern_eng = r'(@media\s*\(min-width:\s*992px\)\s*{.*?\.engineering-standard\s*{)([^}]*)(})'
def fix_eng(match):
    start, content, end = match.groups()
    new_content = '\n        display: grid;\n        grid-template-columns: 1fr 1fr;\n        gap: 4rem;\n        align-items: center;\n        padding: 3rem;'
    return start + new_content + end

css = re.sub(pattern_eng, fix_eng, css, flags=re.DOTALL)

# 4. Explicitly set .portfolio-grid PC layout (50/50)
css = re.sub(r'\.portfolio-grid\s*{\s*display:\s*grid;\s*grid-template-columns:\s*[^;]+;\s*gap:\s*[^;]+;\s*align-items:\s*center;\s*margin:[^;]+;\s*max-width:[^;]+;\s*}', 
             '.portfolio-grid {\n    display: grid;\n    grid-template-columns: 1fr 1fr; /* 50/50 split */\n    gap: 4rem;\n    align-items: center;\n    margin: 2rem auto 0;\n    max-width: 1300px;\n}', 
             css)

# 5. Fix the title font size for Trident Engineering Standard
css = re.sub(r'font-size:\s*3\.75rem\s*!important;', 'font-size: 3.75rem !important;', css)
# Ensure no 5rem override remains
css = css.replace('font-size: 5rem !important;', 'font-size: 3.75rem !important;')

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)
print("Updated style.css")

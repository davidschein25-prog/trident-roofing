import re

with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Pattern for the PC engineering-standard rule
# We want to remove the grid layout and restore the centered large image
pattern = r'@media\s*\(min-width:\s*992px\)\s*{\s*\.engineering-standard\s*{[^}]*display:\s*grid;[^}]*}\s*\.standard-header\s*h3,\s*\.standard-header\s*p\s*{[^}]*text-align:\s*left;[^}]*}\s*\.standard-header\s*h3\s*{[^}]*font-size:\s*5rem\s*!important;[^}]*}\s*\.blueprint-outer\s*{[^}]*max-width:\s*500px;[^}]*}\s*}'

new_pc_rule = """
@media (min-width: 992px) {
    .engineering-standard {
        display: block !important;
        padding: 5rem 3rem !important;
        max-width: 1400px !important;
        margin: 4rem auto !important;
        background: rgba(107, 142, 155, 0.05) !important;
        border-radius: 40px !important;
    }
    .standard-header h3, .standard-header p {
        text-align: center !important;
        max-width: 900px !important;
        margin-left: auto !important;
        margin-right: auto !important;
    }
    .standard-header h3 {
        font-size: 5rem !important;
        line-height: 1.1 !important;
        margin-bottom: 2rem !important;
    }
    .blueprint-container {
        max-width: 1000px !important; /* Restore large size */
        margin: 4rem auto 0 !important;
        box-shadow: 0 30px 60px rgba(0,0,0,0.15) !important;
    }
}"""

# If the regex is too brittle, I'll just find the start of the media query
if "@media (min-width: 992px)" in css:
    # Find the block related to engineering-standard and replace it
    # For safety, I'll just append the new rule at the very bottom of the file with !important tags
    css += "\n\n/* Restore Portfolio Size Overrides */\n" + new_pc_rule

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)
print("Updated style.css")

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

indicator_html = """
                <div class="scroll-indicator">
                    <span class="scroll-text">Scroll to Explore</span>
                    <i class="fas fa-chevron-down"></i>
                </div>
            </div>
        </section>"""

# Replace the specific closing sequence
html = html.replace('            </div>\n        </section>', indicator_html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated index.html")

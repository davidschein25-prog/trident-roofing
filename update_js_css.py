import os

# --- Update app.js ---
app_path = "c:\\Users\\Admin\\Documents\\dev stuff\\Roofing\\js\\app.js"
with open(app_path, "r", encoding="utf-8") as f:
    app_js = f.read()

app_js = app_js.replace("initEstimateTool();\n", "")
app_js = app_js.replace("initAboutCounter();\n", "initAboutCounter();\n    initTridentEdge();\n")

# Trident Edge click logic
trident_edge_js = """
/**
 * Trident Edge Click Details
 */
function initTridentEdge() {
    const items = document.querySelectorAll('.clickable-edge');
    items.forEach(item => {
        item.addEventListener('click', () => {
            const detail = item.getAttribute('data-detail');
            if(detail) {
                alert(detail); // Simple alert for now, could be a tooltip or modal
            }
        });
    });
}
"""
app_js += trident_edge_js

# Update service modal data
old_service_data = """        'eavestroughs': {
            title: 'Seamless Water Management',
            subtitle: 'Foundation Protection',
            description: 'Our seamless aluminum eavestroughs are custom-formed on-site to provide a perfect fit and eliminate leak-prone joints.',
            features: [
                'Heavy-Duty Aluminum: Resists denting and sagging.',
                'Precision Pitching: Ensures total drainage.',
                'Secure Hangers: Spaced for maximum snow load support.',
                'Custom Mitres: Hand-cut corners for a leak-proof finish.',
                'Optimized Downspouts: Channelling water away from foundation.'
            ],
            cta: 'Schedule an Eavestrough Consultation'
        },
        'gutter-guards': {
            title: 'Alu-Rex Gutter Protection',
            subtitle: 'Never Clean Gutters Again',
            description: 'We install the industry-leading Alu-Rex system, which adds structural strength to your gutters while preventing debris accumulation.',
            features: [
                'No Clogs: Keeps leaves, needles, and debris out.',
                'Structural Reinforcement: Protects gutters from snow/ice weight.',
                'Optimal Flow: Handles heavy rainfall without overflowing.',
                'Pest Prevention: Seals out birds and rodents.',
                'Lifetime Performance: Built to last the life of the home.'
            ],
            cta: 'Schedule a Gutter Guard Consultation'
        }"""

new_service_data = """        'eavestroughs': {
            title: 'Seamless Water Management',
            subtitle: 'Foundation Protection',
            description: 'Our seamless aluminum eavestroughs combined with Alu-Rex leaf protection systems provide a perfect fit and eliminate leak-prone joints and clogs.',
            features: [
                'Heavy-Duty Aluminum: Resists denting and sagging.',
                'Alu-Rex Guards: Keeps leaves, needles, and debris out.',
                'Structural Reinforcement: Protects gutters from snow/ice weight.',
                'Custom Mitres: Hand-cut corners for a leak-proof finish.',
                'Optimized Downspouts: Channelling water away from foundation.'
            ],
            cta: 'Schedule an Eavestrough Consultation'
        },
        'skylights': {
            title: 'Skylights & Sun Tunnels',
            subtitle: 'Natural Light, Zero Leaks',
            description: 'Professional installation of Velux skylights and sun tunnels. We ensure a perfect, leak-free integration with your roofing system.',
            features: [
                'Velux Certified: Installed to exact manufacturer specs.',
                'Energy Efficient: Premium glass coatings reduce heat transfer.',
                'Leak-Free Guarantee: Advanced flashing systems ensure watertight seals.',
                'Natural Light: Drastically transform dark spaces.',
                'Ventilation Options: Available in manual or solar-powered venting models.'
            ],
            cta: 'Schedule a Skylight Consultation'
        },
        'specialty': {
            title: 'Custom Exterior Solutions',
            subtitle: 'Comprehensive Protection',
            description: 'Beyond standard systems, we offer specialized upgrades to perfect your home\\'s exterior performance and aesthetic.',
            features: [
                'Blown-In Insulation: Maximize attic thermal efficiency.',
                'Custom Metal Capping: Protect wood fascia and trim with precision metal.',
                'Technical Flashing: Custom bent lead and aluminum for complex roof transitions.',
                'Heating Cables: Prevent ice dams in problem areas.',
                'Seasonal Accents: Professional holiday lighting installation.'
            ],
            cta: 'Schedule a Custom Solutions Consultation'
        },
        'emergency': {
            title: 'Storm Response & Insurance',
            subtitle: '24/7 Protection & Claim Assistance',
            description: 'Active leak or storm damage? We provide 24/7 emergency mitigation and full insurance claim assistance to ensure you are fully covered and stress-free.',
            features: [
                '24/7 Dispatch: Rapid response to prevent interior damage.',
                'Temporary Tarping: Secure your roof immediately.',
                'Comprehensive Inspection: Full documentation of storm damage.',
                'Claim Assistance: We work directly with your adjuster.',
                'Restoration: Full system replacement approved by insurance.'
            ],
            cta: 'Get Immediate Assistance'
        }"""
app_js = app_js.replace(old_service_data, new_service_data)

# route modal cta to contact.html
app_js = app_js.replace('<a href="#quote" class="btn btn-primary modal-cta" id="modal-cta-btn">${data.cta}</a>', '<a href="contact.html" class="btn btn-primary modal-cta" id="modal-cta-btn">${data.cta}</a>')

with open(app_path, "w", encoding="utf-8") as f:
    f.write(app_js)


# --- Update contact.html ---
contact_path = "c:\\Users\\Admin\\Documents\\dev stuff\\Roofing\\contact.html"
with open(contact_path, "r", encoding="utf-8") as f:
    contact_html = f.read()

old_form = """                            <div class="form-group">
                                <label for="first-name">Your First Name</label>
                                <input type="text" id="first-name" name="first-name" placeholder="Enter your first name" required>
                            </div>
                            
                            <div class="form-group">
                                <label for="email">Your Email Address*</label>
                                <input type="email" id="email" name="email" placeholder="Enter your email address" required>
                            </div>

                            <div class="form-group">
                                <label for="service-type">Interested System</label>
                                <select id="service-type" name="service-type">
                                    <option value="roofing">Roofing System</option>
                                    <option value="siding">Siding System</option>
                                    <option value="eavestroughs">Eavestroughs</option>
                                    <option value="gutter-guards">Gutter Protection</option>
                                    <option value="emergency">Emergency Response</option>
                                </select>
                            </div>

                            <div class="form-group">
                                <label for="message">Your Message*</label>
                                <textarea id="message" name="message" rows="5" placeholder="Describe your project needs" required></textarea>
                            </div>

                            <button type="submit" class="btn btn-primary btn-xl w-100">
                                Submit Your Request <i class="fas fa-paper-plane" style="margin-left: 10px;"></i>
                            </button>"""

new_form = """                            <div class="form-group">
                                <label for="first-name">Your Name*</label>
                                <input type="text" id="first-name" name="name" placeholder="Enter your full name" required>
                            </div>
                            
                            <div class="form-group">
                                <label for="phone">Your Phone Number*</label>
                                <input type="tel" id="phone" name="phone" placeholder="Enter your phone number" required>
                            </div>
                            
                            <div class="form-group">
                                <label for="email">Your Email Address*</label>
                                <input type="email" id="email" name="email" placeholder="Enter your email address" required>
                            </div>
                            
                            <div class="form-group">
                                <label for="address">Property Address*</label>
                                <input type="text" id="address" name="address" placeholder="Enter your property address" required>
                            </div>
                            
                            <div class="form-group">
                                <label style="display: flex; align-items: center; gap: 10px; cursor: pointer; color: var(--text-main);">
                                    <input type="checkbox" name="insurance_claim" value="yes" style="width: auto; margin-bottom: 0;">
                                    Is this an insurance claim?
                                </label>
                            </div>

                            <div class="form-group">
                                <label for="service-type">Interested System(s)</label>
                                <select id="service-type" name="service-type" multiple style="height: 120px; color: var(--accent-blue);">
                                    <option value="roofing">Roofing System</option>
                                    <option value="siding">Siding System</option>
                                    <option value="eavestroughs">Eavestroughs & Gutter Guards</option>
                                    <option value="skylights">Skylights & Sun Tunnels</option>
                                    <option value="specialty">Custom Exterior Solutions</option>
                                    <option value="emergency">Emergency Response</option>
                                </select>
                                <small style="color: var(--text-dim);">Hold Ctrl (or Cmd) to select multiple</small>
                            </div>

                            <div class="form-group">
                                <label for="message">Your Message*</label>
                                <textarea id="message" name="message" rows="4" placeholder="Describe your project needs" required></textarea>
                            </div>

                            <button type="submit" class="btn btn-primary btn-xl w-100">
                                Submit Your Request <i class="fas fa-paper-plane" style="margin-left: 10px;"></i>
                            </button>"""

contact_html = contact_html.replace(old_form, new_form)
contact_html = contact_html.replace('href="index.html#services" class="nav-link"', 'href="index.html" class="nav-link"')

with open(contact_path, "w", encoding="utf-8") as f:
    f.write(contact_html)

# --- Update style.css ---
css_path = "c:\\Users\\Admin\\Documents\\dev stuff\\Roofing\\css\\style.css"
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

# Add scroll-indicator style if not exists
if ".scroll-indicator {" not in css:
    css += """
/* Scroll Indicator */
.scroll-indicator {
    position: absolute;
    bottom: 2rem;
    left: 50%;
    transform: translateX(-50%);
    z-index: 20;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0.5rem;
    color: var(--text-dim);
    font-size: 0.8rem;
    text-transform: uppercase;
    letter-spacing: 0.15em;
    animation: bounce-glide 2s ease-in-out infinite;
    transition: opacity 0.5s ease;
    background: rgba(255, 255, 255, 0.1);
    padding: 10px 20px;
    border-radius: 30px;
    backdrop-filter: blur(5px);
}

.scroll-indicator:hover {
    background: rgba(255, 255, 255, 0.2);
}

@keyframes bounce-glide {
    0%, 100% { transform: translateX(-50%) translateY(0); }
    50% { transform: translateX(-50%) translateY(10px); }
}

.scroll-text {
    font-weight: 600;
}
"""

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css)


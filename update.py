import os

path = "c:\\Users\\Admin\\Documents\\dev stuff\\Roofing\\index.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Favicon
content = content.replace(
    '<title>Trident Roofing & Exteriors | Premium Exterior Engineering Ontario</title>',
    '<title>Trident Roofing & Exteriors | Premium Exterior Engineering Ontario</title>\\n    <link rel="icon" type="image/png" href="assets/logo.png">'
)

# 2. Hero Phases
old_phases = """                        <div class="hero-phase active" data-phase="1">
                            <span class="phase-tag">The Problem</span>
                            <h1>Your Roof Is <br><span class="text-accent">Aging Out</span></h1>
                            <p>Weather damage, curling shingles, and hidden leaks are silently destroying your home's value.</p>
                        </div>
                        <div class="hero-phase" data-phase="2">
                            <span class="phase-tag">Step 1: Tear-Off</span>
                            <h1>We Strip It <br><span class="text-accent">Down to Deck</span></h1>
                            <p>No shortcuts. We remove all old shingles down to the plywood decking to inspect for hidden rot and damage.</p>
                        </div>
                        <div class="hero-phase" data-phase="3">
                            <span class="phase-tag">Step 2: Underlayment</span>
                            <h1>Ice & Water <br><span class="text-accent">Shield System</span></h1>
                            <p>Synthetic underlayment and ice & water shield rolled across the entire deck — your critical moisture barrier before a single shingle goes down.</p>
                        </div>
                        <div class="hero-phase" data-phase="4">
                            <span class="phase-tag">Step 3: Shingle Installation</span>
                            <h1>Precision <br><span class="text-accent">Craftsmanship</span></h1>
                            <p>Architectural-grade shingles installed on top of the underlayment by master-certified technicians. Every row nailed to spec.</p>
                        </div>
                        <div class="hero-phase" data-phase="5">
                            <span class="phase-tag">Roof Complete</span>
                            <h1>Sealed & <br><span class="text-accent">Protected</span></h1>
                            <p>Your new architectural roof system is complete — drip edge, ridge vents, and flashing all installed to manufacturer spec.</p>
                        </div>
                        <div class="hero-phase" data-phase="6">
                            <span class="phase-tag">Step 5: Siding</span>
                            <h1>Premium Cladding<br><span class="text-accent">Systems</span></h1>
                            <p>Old siding removed, house wrap inspected, and Westlake Royal architectural-grade siding fitted with precision corners and clean trim work.</p>
                        </div>
                        <div class="hero-phase" data-phase="7">
                            <span class="phase-tag">Step 6: Eavestroughs & Gutter Guards</span>
                            <h1>Total Exterior <br><span class="text-accent">Protection</span></h1>
                            <p>Seamless aluminum eavestroughs and Alu-Rex gutter guards — the final layer that channels water away from your foundation year-round.</p>
                        </div>"""

new_phases = """                        <div class="hero-phase active" data-phase="1">
                            <span class="phase-tag">Protect Your Family</span>
                            <h1>Your Roof is Your <br><span class="text-accent">First Line of Defense</span></h1>
                            <p>Don't wait for expensive leaks or catastrophic damage. A premium roofing system protects your biggest investment and gives you peace of mind.</p>
                        </div>
                        <div class="hero-phase" data-phase="2">
                            <span class="phase-tag">Long-Term Savings</span>
                            <h1>An Investment That <br><span class="text-accent">Pays Off</span></h1>
                            <p>We do things differently. While others cut corners, our engineered systems are built to last, preventing costly future repairs and improving your monthly efficiency.</p>
                        </div>
                        <div class="hero-phase" data-phase="3">
                            <span class="phase-tag">Appreciate Your Home</span>
                            <h1>Increase Your <br><span class="text-accent">Property Value</span></h1>
                            <p>A high-performance exterior transformation dramatically improves curb appeal and instantly increases the resale value of your home.</p>
                        </div>
                        <div class="hero-phase" data-phase="4">
                            <span class="phase-tag">Precision Craftsmanship</span>
                            <h1>Built Right, <br><span class="text-accent">The First Time</span></h1>
                            <p>We charge a premium because our work demands it. Master-certified technicians ensure every shingle, vent, and flashing is installed to exact specifications.</p>
                        </div>
                        <div class="hero-phase" data-phase="5">
                            <span class="phase-tag">Peace of Mind</span>
                            <h1>Fully Licensed & <br><span class="text-accent">Insured Protection</span></h1>
                            <p>Sleep easy knowing your home is secured by a fully insured team with a $5,000,000 liability policy and comprehensive system warranties.</p>
                        </div>
                        <div class="hero-phase" data-phase="6">
                            <span class="phase-tag">Insurance Claim Assistance</span>
                            <h1>We Handle The <br><span class="text-accent">Heavy Lifting</span></h1>
                            <p>Dealing with storm damage? We provide expert insurance claim assistance to ensure you get the coverage you deserve.</p>
                        </div>
                        <div class="hero-phase" data-phase="7">
                            <span class="phase-tag">Total Enclosure</span>
                            <h1>Engineered To <br><span class="text-accent">Outlast</span></h1>
                            <p>From seamless eavestroughs to architectural siding, our holistic approach ensures every component works together for ultimate protection.</p>
                        </div>"""

content = content.replace(old_phases, new_phases)

# 3. Hero image 4 update
content = content.replace('src="assets/hero_4.png"', 'src="assets/hero_4_new.png"')

# 4. Scroll for more info indicator
scroll_html = """                <div class="hero-phase-dots">
                    <div class="phase-dot active" data-dot="1"></div>
                    <div class="phase-dot" data-dot="2"></div>
                    <div class="phase-dot" data-dot="3"></div>
                    <div class="phase-dot" data-dot="4"></div>
                    <div class="phase-dot" data-dot="5"></div>
                    <div class="phase-dot" data-dot="6"></div>
                    <div class="phase-dot" data-dot="7"></div>
                </div>
                
                <div class="scroll-indicator">
                    <div class="scroll-text">Scroll for more info</div>
                    <i class="fas fa-chevron-down"></i>
                </div>"""
content = content.replace('                <div class="hero-phase-dots">\\n                    <div class="phase-dot active" data-dot="1"></div>\\n                    <div class="phase-dot" data-dot="2"></div>\\n                    <div class="phase-dot" data-dot="3"></div>\\n                    <div class="phase-dot" data-dot="4"></div>\\n                    <div class="phase-dot" data-dot="5"></div>\\n                    <div class="phase-dot" data-dot="6"></div>\\n                    <div class="phase-dot" data-dot="7"></div>\\n                </div>', scroll_html)

# 5. Trust Carousel Update
old_trust_track = """                        <div class="trust-track">
                            <div class="trust-item"><i class="fas fa-certificate"></i> GAF Certified</div>
                            <div class="trust-item"><i class="fas fa-shield-alt"></i> IKO Approved</div>
                            <div class="trust-item"><i class="fas fa-check-double"></i> Westlake Royal</div>
                            <div class="trust-item"><i class="fas fa-hard-hat"></i> WSIB Compliant</div>
                            <div class="trust-item"><i class="fas fa-tools"></i> Velux Specialist</div>
                            <div class="trust-item"><i class="fas fa-star"></i> 5-Star Rated</div>
                            <!-- Duplicate for infinite loop -->
                            <div class="trust-item"><i class="fas fa-certificate"></i> GAF Certified</div>
                            <div class="trust-item"><i class="fas fa-shield-alt"></i> IKO Approved</div>
                            <div class="trust-item"><i class="fas fa-check-double"></i> Westlake Royal</div>
                            <div class="trust-item"><i class="fas fa-hard-hat"></i> WSIB Compliant</div>
                            <div class="trust-item"><i class="fas fa-tools"></i> Velux Specialist</div>
                            <div class="trust-item"><i class="fas fa-star"></i> 5-Star Rated</div>
                        </div>"""

new_trust_track = """                        <div class="trust-track">
                            <div class="trust-item"><i class="fas fa-shield-alt"></i> IKO Approved</div>
                            <div class="trust-item"><i class="fas fa-check-double"></i> Westlake Royal</div>
                            <div class="trust-item"><i class="fas fa-tools"></i> Velux Specialist</div>
                            <div class="trust-item"><i class="fas fa-tint"></i> Alu-Rex Preferred</div>
                            <div class="trust-item"><i class="fas fa-file-invoice-dollar"></i> Insurance Claim Assistance</div>
                            <div class="trust-item"><i class="fas fa-check-circle"></i> Fully Insured to $5M</div>
                            <!-- Duplicate for infinite loop -->
                            <div class="trust-item"><i class="fas fa-shield-alt"></i> IKO Approved</div>
                            <div class="trust-item"><i class="fas fa-check-double"></i> Westlake Royal</div>
                            <div class="trust-item"><i class="fas fa-tools"></i> Velux Specialist</div>
                            <div class="trust-item"><i class="fas fa-tint"></i> Alu-Rex Preferred</div>
                            <div class="trust-item"><i class="fas fa-file-invoice-dollar"></i> Insurance Claim Assistance</div>
                            <div class="trust-item"><i class="fas fa-check-circle"></i> Fully Insured to $5M</div>
                        </div>"""
content = content.replace(old_trust_track, new_trust_track)

# 6. Trident Edge text
old_trident_box = """                    <div class="comp-box trident-box reveal" style="transition-delay: 0.1s;">
                        <h3 class="mb-md" style="color: var(--accent-blue);">Trident Engineering</h3>
                        <ul style="list-style: none;">
                            <li class="mb-sm"><i class="fas fa-check-circle" style="color: var(--accent-blue);"></i> <span>Advanced No-Heat Systems</span></li>
                            <li class="mb-sm"><i class="fas fa-check-circle" style="color: var(--accent-blue);"></i> <span>Total Exterior Enclosure mindset</span></li>
                            <li class="mb-sm"><i class="fas fa-check-circle" style="color: var(--accent-blue);"></i> <span>Architectural-grade materials</span></li>
                            <li class="mb-sm"><i class="fas fa-check-circle" style="color: var(--accent-blue);"></i> <span>Technical consultation approach</span></li>
                        </ul>
                    </div>"""

new_trident_box = """                    <div class="comp-box trident-box reveal" style="transition-delay: 0.1s;">
                        <h3 class="mb-md" style="color: var(--accent-blue);">Trident Engineering</h3>
                        <ul style="list-style: none;">
                            <li class="mb-sm clickable-edge" data-detail="Our advanced strategies ensure roofs last 50%+ longer than competitors. We use limited caulking and prefer technical flashing bending to prevent long-term failure."><i class="fas fa-check-circle" style="color: var(--accent-blue);"></i> <span>Built to last 50%+ longer</span></li>
                            <li class="mb-sm clickable-edge" data-detail="We utilize neoprene screws for superior weather resistance and longevity compared to standard fasteners."><i class="fas fa-check-circle" style="color: var(--accent-blue);"></i> <span>Advanced fastening systems</span></li>
                            <li class="mb-sm clickable-edge" data-detail="Precision matters. We use full pieces with hand mitres and better cuts/overlaps, never relying on small scrap pieces that compromise integrity."><i class="fas fa-check-circle" style="color: var(--accent-blue);"></i> <span>Precision craftsmanship & hand mitres</span></li>
                            <li class="mb-sm clickable-edge" data-detail="We charge a premium because we deliver premium value. Our comprehensive approach saves you money in the long run by eliminating premature replacements."><i class="fas fa-check-circle" style="color: var(--accent-blue);"></i> <span>True long-term value</span></li>
                        </ul>
                        <p class="text-sm text-center mt-sm" style="color: var(--text-dim);"><em>* Click an item to learn more</em></p>
                    </div>"""
content = content.replace(old_trident_box, new_trident_box)

old_edge_title = """                <h2 class="section-title reveal">The Trident Edge</h2>
                <p class="section-subtitle reveal">Why engineered systems outlast standard roofing.</p>"""
new_edge_title = """                <h2 class="section-title reveal">The Trident Edge</h2>
                <p class="section-subtitle reveal">Why engineered systems outlast standard roofing.</p>
                <div class="text-center mb-lg reveal">
                    <p style="max-width: 800px; margin: 0 auto; line-height: 1.6;">We aim to make our projects last <strong>50%+ longer</strong> than our competition using advanced strategies designed to limit long term failure. Click on the comparison below to learn why Trident is worth the premium price.</p>
                </div>"""
content = content.replace(old_edge_title, new_edge_title)

# Add CTA to Trident Edge
content = content.replace(
    '<div class="grid-3 reveal-group">',
    '<div class="text-center mt-lg mb-lg reveal"><p class="mb-md"><strong>Trident does it best. Protect your home the right way.</strong></p><a href="contact.html" class="btn btn-primary">Get Your Premium Quote</a></div>\\n                <div class="grid-3 reveal-group">'
)

# 7. Engineering Standard Image & Hotspots
old_blueprint = '<img src="assets/blueprint.png" alt="Trident Engineering Blueprint" class="blueprint-img">'
new_blueprint = '<img src="assets/vector_house.png" alt="Trident Engineering Vector House" class="blueprint-img" style="max-width: 80%; margin: 0 auto; display: block;">'
content = content.replace(old_blueprint, new_blueprint)

old_hotspots = """                            <!-- Hotspot 1: Ridge Vent -->
                            <div class="hotspot" style="top: 15%; left: 81%;">
                                <div class="hotspot-pulse"></div>
                                <div class="hotspot-label">
                                    <h4>Ridge Ventilation</h4>
                                    <p>Continuous airflow prevents attic heat buildup and deck rot.</p>
                                </div>
                            </div>

                            <!-- Hotspot 2: Asphalt Shingles -->
                            <div class="hotspot" style="top: 30%; left: 62%;">
                                <div class="hotspot-pulse"></div>
                                <div class="hotspot-label">
                                    <h4>Asphalt Shingles</h4>
                                    <p>IKO Dynasty architectural shingles with ArmourZone® for 210km/h wind protection.</p>
                                </div>
                            </div>

                            <!-- Hotspot 3: Synthetic Underlayment -->
                            <div class="hotspot" style="top: 39%; left: 49%;">
                                <div class="hotspot-pulse"></div>
                                <div class="hotspot-label">
                                    <h4>High-Perf Underlayment</h4>
                                    <p>Synthetic barrier that breathes while blocking 100% of moisture.</p>
                                </div>
                            </div>

                            <!-- Hotspot 4: Plywood Sheathing -->
                            <div class="hotspot" style="top: 45%; left: 39%;">
                                <div class="hotspot-pulse"></div>
                                <div class="hotspot-label">
                                    <h4>Plywood Sheathing</h4>
                                    <p>The structural foundation. We perform a 100% deck inspection on every project.</p>
                                </div>
                            </div>

                            <!-- Hotspot 5: Precision Drip Edge -->
                            <div class="hotspot" style="top: 61%; left: 19%;">
                                <div class="hotspot-pulse"></div>
                                <div class="hotspot-label">
                                    <h4>Precision Drip Edge</h4>
                                    <p>Architectural flashing that directs water safely into the eavestroughs.</p>
                                </div>
                            </div>

                            <!-- Hotspot 6: Ice & Water Shield -->
                            <div class="hotspot" style="top: 34.5%; left: 55.5%;">
                                <div class="hotspot-pulse"></div>
                                <div class="hotspot-label">
                                    <h4>Ice & Water Shield</h4>
                                    <p>Critical rubberized membrane protection for all valleys and eaves.</p>
                                </div>
                            </div>

                            <!-- Hotspot 7: Soffit Ventilation -->
                            <div class="hotspot" style="top: 68%; left: 28%;">
                                <div class="hotspot-pulse"></div>
                                <div class="hotspot-label">
                                    <h4>Soffit Intake Vent</h4>
                                    <p>Ensures fresh air intake to balance attic temperatures and prevent ice dams.</p>
                                </div>
                            </div>"""

new_hotspots = """                            <!-- Hotspot 1: Ridge Vent -->
                            <div class="hotspot" style="top: 10%; left: 50%;">
                                <div class="hotspot-pulse"></div>
                                <div class="hotspot-label">
                                    <h4>Premium Ridge Ventilation</h4>
                                    <p>We use top-tier continuous airflow vents installed with precise measurements to permanently prevent attic heat buildup and deck rot.</p>
                                </div>
                            </div>

                            <!-- Hotspot 2: Asphalt Shingles -->
                            <div class="hotspot" style="top: 25%; left: 30%;">
                                <div class="hotspot-pulse"></div>
                                <div class="hotspot-label">
                                    <h4>Premium Shingle Systems</h4>
                                    <p>Architectural shingles installed exclusively with 6-nail patterns and precise edge alignment for ultimate wind protection and longevity.</p>
                                </div>
                            </div>

                            <!-- Hotspot 3: Eavestroughs & Gutter Guards -->
                            <div class="hotspot" style="top: 45%; left: 80%;">
                                <div class="hotspot-pulse"></div>
                                <div class="hotspot-label">
                                    <h4>Seamless Eavestroughs</h4>
                                    <p>Custom-formed seamless aluminum with Alu-Rex guard systems, perfectly pitched for high-capacity flow.</p>
                                </div>
                            </div>

                            <!-- Hotspot 4: Siding & Cladding -->
                            <div class="hotspot" style="top: 65%; left: 20%;">
                                <div class="hotspot-pulse"></div>
                                <div class="hotspot-label">
                                    <h4>Architectural Siding</h4>
                                    <p>Premium Westlake Royal siding with specialized house wrap and meticulously hand-cut corner mitres.</p>
                                </div>
                            </div>

                            <!-- Hotspot 5: Underlayment & Shield -->
                            <div class="hotspot" style="top: 35%; left: 65%;">
                                <div class="hotspot-pulse"></div>
                                <div class="hotspot-label">
                                    <h4>Maximum Protection Shield</h4>
                                    <p>High-performance synthetic underlayment and double-layered ice & water shield in critical valleys.</p>
                                </div>
                            </div>"""
content = content.replace(old_hotspots, new_hotspots)

# 8. About Us
old_about = """                <div class="about-content reveal-group">
                    <h2 class="section-title reveal" style="text-align: left; margin-left: 0;">20+ Years of Engineering Excellence</h2>
                    <p class="section-subtitle reveal" style="text-align: left; margin-left: 0;">Your Trusted Roofing & Exteriors Experts</p>
                    <p class="mb-md reveal" style="font-size: 1.1rem; line-height: 1.7;">Your home deserves the best care, and we deliver it by specializing in roofing, siding, soffit, fascia, eavestroughs, and gutter guards.</p>
                    <p class="mb-md reveal">We bring in-depth knowledge and hands-on experience to **water flow systems** (from your roof to your eavestroughs and siding) and **ventilation systems** (from your roof and vents to insulation and soffits).</p>
                    <p class="mb-md reveal">Unlike many profit-driven companies that cut corners, we build on a foundation of trust and quality. We take pride in our professionalism and would be more than happy to walk you through why our work will outlast our competitors.</p>
                    <div class="about-cta reveal" style="margin-top: 2rem;">
                        <a href="contact.html" class="btn btn-primary">Free Inspection & Quote</a>
                    </div>
                </div>
                <div class="about-visual reveal" style="transition-delay: 0.2s;">
                    <div class="logo-showcase-card">
                        <img src="assets/logo.png" alt="Trident Roofing Logo" class="about-logo">
                        <div class="exp-badge-premium">
                            <span class="exp-num"><span id="exp-counter" data-target="20">0</span>+</span>
                            <span class="exp-text">YEARS</span>
                        </div>
                    </div>
                </div>"""

new_about = """                <div class="about-content reveal-group">
                    <h2 class="section-title reveal" style="text-align: left; margin-left: 0;">Fully Licensed and Insured Excellence</h2>
                    <p class="section-subtitle reveal" style="text-align: left; margin-left: 0;">Your Trusted Roofing & Exteriors Experts</p>
                    <p class="mb-md reveal" style="font-size: 1.1rem; line-height: 1.7;">Your home deserves the best care, and we deliver it by specializing in roofing, siding, soffit, fascia, eavestroughs, and skylights.</p>
                    <p class="mb-md reveal">Trident prides itself on utilizing premium, top-tier products combined with unmatched craftsmanship. This dedication translates to a significant longevity improvement over other companies. We bring in-depth knowledge to advanced water flow and ventilation systems.</p>
                    <p class="mb-md reveal">Our extensive service area covers the heart of Ontario, including <strong>London, St. Thomas, Woodstock, Kitchener-Waterloo, Cambridge, and surrounding communities.</strong></p>
                    <div class="about-cta reveal" style="margin-top: 2rem;">
                        <p class="mb-sm"><strong>Let us protect your home for the next 50 years. We can help.</strong></p>
                        <a href="contact.html" class="btn btn-primary">Free Inspection & Quote</a>
                    </div>
                </div>
                <div class="about-visual reveal" style="transition-delay: 0.2s;">
                    <div class="logo-showcase-card">
                        <img src="assets/logo.png" alt="Trident Roofing Logo" class="about-logo">
                        <div class="exp-badge-premium" style="background: var(--accent-blue); padding: 1.5rem; border-radius: 50%;">
                            <i class="fas fa-shield-alt" style="font-size: 3rem; color: #fff;"></i>
                        </div>
                    </div>
                </div>"""
content = content.replace(old_about, new_about)

# 9. Services
old_services = """                    <div class="service-card-premium reveal" data-service="eavestroughs">
                        <div class="image-box">
                            <img src="assets/service_eavestrough_new.png" alt="Eavestrough Installation">
                        </div>
                        <div class="content-box">
                            <h3>Eavestroughs</h3>
                            <p>Seamless aluminum eavestroughs custom-formed on-site. Proper slope, secure hangers, and clean downspout routing.</p>
                            <button class="nav-link service-modal-trigger" data-service="eavestroughs">Explore System <i class="fas fa-arrow-right"></i></button>
                        </div>
                    </div>
                    <div class="service-card-premium reveal" data-service="gutter-guards">
                        <div class="image-box">
                            <img src="assets/service_gutter_guard_new.png" alt="Gutter Guard Installation">
                        </div>
                        <div class="content-box">
                            <h3>Gutter Guards</h3>
                            <p>Alu-Rex leaf protection systems that eliminate clogs and protect your foundation from water damage year-round.</p>
                            <button class="nav-link service-modal-trigger" data-service="gutter-guards">Explore System <i class="fas fa-arrow-right"></i></button>
                        </div>
                    </div>"""

new_services = """                    <div class="service-card-premium reveal service-modal-trigger" data-service="eavestroughs" style="cursor: pointer;">
                        <div class="image-box">
                            <img src="assets/service_eavestrough_new.png" alt="Eavestrough Installation">
                        </div>
                        <div class="content-box">
                            <h3>Eavestroughs & Gutter Guards</h3>
                            <p>Seamless aluminum eavestroughs combined with Alu-Rex leaf protection systems. Proper slope and clog-free foundation protection.</p>
                            <button class="nav-link">Explore System <i class="fas fa-arrow-right"></i></button>
                        </div>
                    </div>
                    <div class="service-card-premium reveal service-modal-trigger" data-service="skylights" style="cursor: pointer;">
                        <div class="image-box">
                            <img src="assets/service_gutter_guard_new.png" alt="Skylights and Sun Tunnels">
                        </div>
                        <div class="content-box">
                            <h3>Skylights & Sun Tunnels</h3>
                            <p>Professional installation of Velux skylights and sun tunnels. We ensure a perfect, leak-free integration with your roofing system.</p>
                            <button class="nav-link">Explore System <i class="fas fa-arrow-right"></i></button>
                        </div>
                    </div>
                    <div class="service-card-premium reveal service-modal-trigger" data-service="specialty" style="cursor: pointer;">
                        <div class="image-box">
                            <img src="assets/service_siding.png" alt="Specialty Accents">
                        </div>
                        <div class="content-box">
                            <h3>Custom Exterior Solutions</h3>
                            <p>Enhance your home with blown-in insulation, custom metal capping, technical flashing, and seasonal heating cable installations.</p>
                            <button class="nav-link">Explore System <i class="fas fa-arrow-right"></i></button>
                        </div>
                    </div>"""
content = content.replace(old_services, new_services)

# Need to update other service cards to be clickable too
content = content.replace('<div class="service-card-premium reveal" data-service="roofing">', '<div class="service-card-premium reveal service-modal-trigger" data-service="roofing" style="cursor: pointer;">')
content = content.replace('<div class="service-card-premium reveal" data-service="siding">', '<div class="service-card-premium reveal service-modal-trigger" data-service="siding" style="cursor: pointer;">')

# remove duplicate button classes from roofing/siding
content = content.replace('<button class="nav-link service-modal-trigger" data-service="roofing">', '<button class="nav-link">')
content = content.replace('<button class="nav-link service-modal-trigger" data-service="siding">', '<button class="nav-link">')


# Emergency Service Card
old_emergency = """                    <div class="service-card-premium service-card-emergency reveal" style="transition-delay: 0.4s;">
                        <div class="emergency-banner">
                            <div class="emergency-icon">
                                <i class="fas fa-bolt"></i>
                            </div>
                            <div class="emergency-content">
                                <h3>Storm & Leak Response — 24/7</h3>
                                <p>Active leak or storm damage? Our emergency team responds fast to protect your home from further damage. Call anytime, day or night.</p>
                            </div>
                            <a href="tel:2266800996" class="btn btn-primary"><i class="fas fa-phone-alt"></i> (226) 680-0996</a>
                        </div>
                    </div>"""

new_emergency = """                    <div class="service-card-premium service-card-emergency reveal service-modal-trigger" data-service="emergency" style="transition-delay: 0.4s; cursor: pointer;">
                        <div class="emergency-banner">
                            <div class="emergency-icon">
                                <i class="fas fa-bolt"></i>
                            </div>
                            <div class="emergency-content">
                                <h3>Storm Response & Insurance Claims</h3>
                                <p>Active leak or storm damage? We provide 24/7 emergency mitigation and full insurance claim assistance to ensure you are covered.</p>
                            </div>
                            <div class="emergency-actions" style="display: flex; gap: 1rem; align-items: center; flex-wrap: wrap;">
                                <a href="tel:2266800996" class="btn btn-primary"><i class="fas fa-phone-alt"></i> Call Now</a>
                                <button class="btn btn-secondary">Claim Details <i class="fas fa-arrow-right"></i></button>
                            </div>
                        </div>
                    </div>"""
content = content.replace(old_emergency, new_emergency)


# 10. Estimate removal
start_est = "<!-- Estimate Section -->"
end_est = "</section>"
idx1 = content.find(start_est)
idx2 = content.find(end_est, idx1) + len(end_est)
if idx1 != -1 and idx2 != -1:
    content = content[:idx1] + content[idx2:]


with open(path, "w", encoding="utf-8") as f:
    f.write(content)

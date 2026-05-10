// Initialize Parallax Depth (Option 3)
function initParallax() {
    const items = document.querySelectorAll('.parallax-bg');
    const mobileHub = document.querySelector('.mobile-hub');
    const hero = document.getElementById('hero-runway');
    if (items.length === 0 && !mobileHub) return;

    window.addEventListener('scroll', () => {
        const scrolled = window.pageYOffset;
        
        // Parallax Logic
        items.forEach(item => {
            const rect = item.getBoundingClientRect();
            if (rect.top < window.innerHeight && rect.bottom > 0) {
                const speed = 0.15;
                const yPos = -(scrolled * speed);
                item.style.backgroundPositionY = `calc(50% + ${yPos}px)`;
            }
        });

        // Mobile Hub Visibility Logic (Option 1)
        if (mobileHub && hero) {
            const heroBottom = hero.offsetTop + hero.offsetHeight;
            if (scrolled > heroBottom - 500) { // Appear slightly before hero ends
                mobileHub.classList.add('visible');
            } else {
                mobileHub.classList.remove('visible');
            }
        }
    }, { passive: true });
}

document.addEventListener('DOMContentLoaded', () => {
    initHeroAnimation();
    initEmergencyMode();
    initProjectSlider();
    initEstimateTool();
    initRoofQuiz();
    initRevealAnimations();
    initServiceModals();
    initPortfolioModal();
    initMobileNav();
    initParallax();
    initAboutCounter();
    initMagneticButtons();
});

/**
 * Scroll-Hijacked Cinematic Hero Animation
 * Pins the hero viewport and crossfades through 5 illustration frames
 * based on scroll progress through a 500vh tall "runway" section.
 */
function initHeroAnimation() {
    const runway = document.getElementById('hero-runway');
    if (!runway) return;

    const frames = document.querySelectorAll('.hero-frame');
    const phases = document.querySelectorAll('.hero-phase');
    const dots = document.querySelectorAll('.phase-dot');
    const progressBar = document.getElementById('hero-progress-bar');
    const scrollHint = document.getElementById('scroll-hint');
    const totalPhases = frames.length;
    
    let lastPhase = -1;

    function updateHero() {
        const rect = runway.getBoundingClientRect();
        const runwayHeight = runway.offsetHeight;
        const viewportHeight = window.innerHeight;
        
        // How far we've scrolled into the runway (0 to 1)
        const scrolled = -rect.top;
        const maxScroll = runwayHeight - viewportHeight;
        const progress = Math.max(0, Math.min(1, scrolled / maxScroll));
        
        // Map progress to phase (1-indexed)
        const currentPhase = Math.min(totalPhases, Math.floor(progress * totalPhases) + 1);
        
        // Update progress bar
        if (progressBar) {
            progressBar.style.height = `${progress * 100}%`;
        }
        
        // Hide scroll hint after first scroll
        if (scrollHint) {
            scrollHint.classList.toggle('hidden', progress > 0.05);
        }
        
        // Only update DOM if phase changed
        if (currentPhase !== lastPhase) {
            lastPhase = currentPhase;
            
            // Crossfade frames
            frames.forEach(f => {
                const frameNum = parseInt(f.dataset.frame);
                f.classList.toggle('active', frameNum === currentPhase);
            });
            
            // Switch text phases
            phases.forEach(p => {
                const phaseNum = parseInt(p.dataset.phase);
                p.classList.toggle('active', phaseNum === currentPhase);
            });
            
            // Update dots
            dots.forEach(d => {
                const dotNum = parseInt(d.dataset.dot);
                d.classList.toggle('active', dotNum === currentPhase);
            });
        }
        
        requestAnimationFrame(updateHero);
    }
    
    requestAnimationFrame(updateHero);
}


/**
 * REVEAL ANIMATIONS
 * Standard fade-in-up animations for sections and elements.
 * Supports .reveal-group for staggered children.
 */
function initRevealAnimations() {
    const observerOptions = {
        threshold: 0.15,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                // If it's a group, reveal all children with stagger
                if (entry.target.classList.contains('reveal-group')) {
                    const children = entry.target.querySelectorAll('.reveal');
                    children.forEach((child, index) => {
                        child.style.setProperty('--stagger-index', index);
                        child.classList.add('active');
                    });
                } else {
                    entry.target.classList.add('active');
                }
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    // Track standard reveals and groups
    document.querySelectorAll('.reveal, .reveal-group').forEach(el => observer.observe(el));
}

/**
 * Emergency Mode Toggle
 */
function initEmergencyMode() {
    const toggle = document.getElementById('emergency-toggle');
    if (!toggle) return;

    toggle.addEventListener('click', () => {
        document.body.classList.toggle('emergency-mode');
        const isEmergency = document.body.classList.contains('emergency-mode');
        toggle.innerHTML = isEmergency ? '<i class="fas fa-times"></i> EXIT EMERGENCY' : '<i class="fas fa-bolt"></i> EMERGENCY MODE';
        
        if (isEmergency) {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }
    });
}

/**
 * Before/After Project Slider (Premium Overlay Logic)
 */
function initProjectSlider() {
    const slider = document.getElementById('project-slider');
    if (!slider) return;

    const afterImg = slider.querySelector('.img-after');
    const handle = slider.querySelector('.slider-handle');
    // Pins are now in the slider-outer, not inside the slider-container itself
    const pins = slider.parentElement.querySelectorAll('.p-pin');
    let isDragging = false;
    let animationFrameId = null;


    const updatePins = (percent) => {
        pins.forEach(pin => {
            const pinX = parseFloat(pin.getAttribute('data-x'));
            // Pin is on the "After" side if its X position is less than the reveal percentage
            if (pinX < percent) {
                pin.classList.add('is-success');
            } else {
                pin.classList.remove('is-success');
            }
        });
    };

    const moveSlider = (clientX) => {
        const rect = slider.getBoundingClientRect();
        let x = clientX - rect.left - window.scrollX;
        
        if (x < 0) x = 0;
        if (x > rect.width) x = rect.width;
        
        const percent = (x / rect.width) * 100;
        
        if (animationFrameId) cancelAnimationFrame(animationFrameId);
        animationFrameId = requestAnimationFrame(() => {
            // Uncover After from left to right: inset(0 [remaining-percent] 0 0)
            afterImg.style.clipPath = `inset(0 ${100 - percent}% 0 0)`;
            handle.style.left = `${percent}%`;
            updatePins(percent);
        });
    };

    // Event Listeners
    slider.addEventListener('mousedown', (e) => {
        e.preventDefault();
        isDragging = true;
        moveSlider(e.pageX);
    });

    window.addEventListener('mouseup', () => {
        isDragging = false;
    });

    window.addEventListener('mousemove', (e) => {
        if (!isDragging) return;
        moveSlider(e.pageX);
    });

    // Touch Support
    slider.addEventListener('touchstart', (e) => {
        isDragging = true;
        moveSlider(e.touches[0].pageX);
    }, { passive: false });

    window.addEventListener('touchend', () => {
        isDragging = false;
    });

    window.addEventListener('touchmove', (e) => {
        if (!isDragging) return;
        e.preventDefault();
        moveSlider(e.touches[0].pageX);
    }, { passive: false });
    
    // Init pins at default 50%
    updatePins(50);
}

/**
 * Instant Estimate Tool Logic (Fixed Selector)
 */
function initEstimateTool() {
    const tool = document.getElementById('estimate-tool');
    if (!tool) return;

    const options = tool.querySelectorAll('.option-card');
    const calculateBtn = document.getElementById('calculate-btn');
    const resultBox = document.getElementById('estimate-result');
    const sizeInput = document.getElementById('roof-size');
    
    let selectedType = null;

    options.forEach(opt => {
        opt.addEventListener('click', () => {
            // Remove active from others
            options.forEach(o => o.classList.remove('active-option'));
            opt.classList.add('active-option');
            selectedType = opt.dataset.value;
            
            // Move to step 2
            tool.querySelector('[data-step="1"]').classList.remove('active');
            tool.querySelector('[data-step="2"]').classList.add('active');
        });
    });

    calculateBtn.addEventListener('click', () => {
        const size = parseFloat(sizeInput.value);
        if (!size || !selectedType) return;

        let minRate, maxRate;
        if (selectedType === 'asphalt') { minRate = 6; maxRate = 9; }
        else if (selectedType === 'flat') { minRate = 12; maxRate = 18; }
        else { minRate = 15; maxRate = 25; }

        const min = Math.floor(size * minRate);
        const max = Math.floor(size * maxRate);

        // Count-up animation (Option 2)
        const animateVal = (id, start, end, duration) => {
            const obj = document.getElementById(id);
            if (!obj) return;
            let startTimestamp = null;
            const step = (timestamp) => {
                if (!startTimestamp) startTimestamp = timestamp;
                const progress = Math.min((timestamp - startTimestamp) / duration, 1);
                const value = Math.floor(progress * (end - start) + start);
                obj.innerHTML = value.toLocaleString();
                if (progress < 1) {
                    window.requestAnimationFrame(step);
                }
            };
            window.requestAnimationFrame(step);
        };

        tool.querySelector('[data-step="2"]').classList.remove('active');
        tool.querySelector('[data-step="3"]').classList.add('active');

        animateVal('min-val', 0, min, 1500);
        animateVal('max-val', 0, max, 1500);
    });
}

/**
 * Roof Health Quiz Logic
 */
function initRoofQuiz() {
    const quiz = document.getElementById('roof-quiz');
    if (!quiz) return;

    const steps = quiz.querySelectorAll('.step');
    const options = quiz.querySelectorAll('.option-card');
    const resultTitle = document.getElementById('quiz-result');
    const resultAdvice = document.getElementById('quiz-advice');
    
    let totalScore = 0;
    let currentStep = 1;

    options.forEach(opt => {
        opt.addEventListener('click', () => {
            const points = parseInt(opt.dataset.points);
            totalScore += points;
            
            if (currentStep < steps.length - 1) {
                quiz.querySelector(`[data-quiz-step="${currentStep}"]`).classList.remove('active');
                currentStep++;
                quiz.querySelector(`[data-quiz-step="${currentStep}"]`).classList.add('active');
            } else {
                quiz.querySelector(`[data-quiz-step="${currentStep}"]`).classList.remove('active');
                quiz.querySelector(`[data-quiz-step="4"]`).classList.add('active');
                displayQuizResult(totalScore);
            }
        });
    });

    function displayQuizResult(score) {
        let title, advice;
        if (score <= 2) {
            title = "Score: 90% (Excellent)";
            advice = "Your roof is in great shape. We recommend a proactive inspection in 24 months.";
        } else if (score <= 8) {
            title = "Score: 65% (Warning)";
            advice = "Moderate wear detected. Book an inspection within 30 days.";
        } else {
            title = "Score: 25% (CRITICAL)";
            advice = "High risk of failure. Book an urgent audit immediately.";
        }
    }
}

/**
 * Service Modals Logic
 */
function initServiceModals() {
    const modal = document.getElementById('service-modal');
    const modalBody = document.getElementById('modal-body');
    const closeBtn = document.getElementById('modal-close');
    const triggers = document.querySelectorAll('.service-modal-trigger');

    const serviceData = {
        'roofing': {
            title: 'Advanced Roofing Systems',
            subtitle: 'Engineered for Ontario\'s Extremes',
            description: 'Our roofing systems go beyond simple shingle replacement. We engineer a multi-layered shield designed to withstand heavy snow loads, high winds, and rapid freeze-thaw cycles.',
            features: [
                'Full Tear-Off: We strip to the deck to inspect for rot.',
                'Ice & Water Shield: Critical protection for valleys and eaves.',
                'Synthetic Underlayment: High-performance moisture barrier.',
                'Master Certified Install: Backed by manufacturer warranties.',
                'Canadian-Sourced: Using IKO and Westlake Royal materials.'
            ],
            cta: 'Schedule a Roofing Consultation'
        },
        'siding': {
            title: 'Premium Cladding Systems',
            subtitle: 'Thermal Performance & Curb Appeal',
            description: 'Westlake Royal certified siding systems that provide superior insulation and moisture management while completely transforming your home\'s aesthetic.',
            features: [
                'Rigid Foam Backing: Improved R-value and impact resistance.',
                'Advanced House Wrap: Prevents trapped moisture and rot.',
                'Precision Trim Work: Clean corners and architectural details.',
                'Fade-Resistant Colors: UV-stable technology.',
                'Low Maintenance: Never paint your home again.'
            ],
            cta: 'Schedule a Siding Consultation'
        },
        'eavestroughs': {
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
        }
    };

    triggers.forEach(trigger => {
        trigger.addEventListener('click', (e) => {
            e.stopPropagation();
            const service = trigger.dataset.service;
            const data = serviceData[service];
            if (!data) return;

            modalBody.innerHTML = `
                <div class="modal-subtitle">${data.subtitle}</div>
                <h2>${data.title}</h2>
                <p>${data.description}</p>
                <ul>
                    ${data.features.map(f => `<li><i class="fas fa-check-circle"></i> ${f}</li>`).join('')}
                </ul>
                <a href="#quote" class="btn btn-primary modal-cta" id="modal-cta-btn">${data.cta}</a>
            `;

            modal.classList.add('active');
            document.body.style.overflow = 'hidden';

            // Close modal when CTA is clicked
            document.getElementById('modal-cta-btn').addEventListener('click', () => {
                closeModal();
            });
        });
    });

    const closeModal = () => {
        modal.classList.remove('active');
        document.body.style.overflow = '';
    };

    closeBtn.addEventListener('click', closeModal);
    modal.addEventListener('click', (e) => {
        if (e.target === modal) closeModal();
    });
}

/**
 * CINEMATIC MICRO-INTERACTIONS
 * Implements mouse-tracking spotlight and 3D tilt for multiple card types
 */
function initCinematicInteractions() {
    // Target all premium interactive cards
    const cards = document.querySelectorAll('.service-card-premium, .logo-showcase-card, .contact-info-panel, .contact-form-panel');
    
    cards.forEach(card => {
        // 1. Inject the spotlight element if it doesn't exist
        if (!card.querySelector('.card-spotlight')) {
            const spotlight = document.createElement('div');
            spotlight.className = 'card-spotlight';
            card.prepend(spotlight);
        }

        // 2. Track mouse movement
        card.addEventListener('mousemove', (e) => {
            const rect = card.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;

            // Update CSS variables for the spotlight position
            card.style.setProperty('--mouse-x', `${x}px`);
            card.style.setProperty('--mouse-y', `${y}px`);

            // 3. Calculate 3D Tilt
            const centerX = rect.width / 2;
            const centerY = rect.height / 2;
            
            // Subtle rotation (max ~3-4 degrees)
            const rotateX = (y - centerY) / 25;
            const rotateY = (centerX - x) / 25;

            card.style.transform = `translateY(-12px) rotateX(${rotateX}deg) rotateY(${rotateY}deg)`;
        });

        // 4. Reset on leave
        card.addEventListener('mouseleave', () => {
            card.style.transform = 'translateY(0) rotateX(0deg) rotateY(0deg)';
        });
    });
}

/**
 * Portfolio Detail Modal Logic (Mobile)
 */
function initPortfolioModal() {
    const modal = document.getElementById('portfolio-modal');
    const openBtn = document.getElementById('portfolio-more-btn');
    const closeBtn = document.getElementById('portfolio-modal-close');

    if (!modal || !openBtn || !closeBtn) return;

    openBtn.addEventListener('click', () => {
        modal.classList.add('active');
        document.body.style.overflow = 'hidden';
    });

    const closeModal = () => {
        modal.classList.remove('active');
        document.body.style.overflow = '';
    };

    closeBtn.addEventListener('click', closeModal);
    modal.addEventListener('click', (e) => {
        if (e.target === modal) closeModal();
    });
}

/**
 * Mobile Navigation Toggle
 */
function initMobileNav() {
    const hamburger = document.getElementById('hamburger');
    const nav = document.querySelector('.desktop-nav');
    const links = document.querySelectorAll('.nav-link');

    if (!hamburger || !nav) return;

    hamburger.addEventListener('click', () => {
        hamburger.classList.toggle('active');
        nav.classList.toggle('active');
    });

    // Close menu when clicking links
    links.forEach(link => {
        link.addEventListener('click', () => {
            hamburger.classList.remove('active');
            nav.classList.remove('active');
        });
    });
}

/**
 * Initialize About Counter (Option - Dynamic Experience)
 */
function initAboutCounter() {
    const counter = document.getElementById('exp-counter');
    if (!counter) return;

    const target = parseInt(counter.dataset.target);
    let started = false;

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting && !started) {
                started = true;
                
                let startTimestamp = null;
                const duration = 2000;
                const step = (timestamp) => {
                    if (!startTimestamp) startTimestamp = timestamp;
                    const progress = Math.min((timestamp - startTimestamp) / duration, 1);
                    counter.innerHTML = Math.floor(progress * target);
                    if (progress < 1) {
                        window.requestAnimationFrame(step);
                    }
                };
                window.requestAnimationFrame(step);
            }
        });
    }, { threshold: 0.1 });

    observer.observe(counter);
}

/**
 * Magnetic Buttons (Option 1 - Desktop Only)
 */
function initMagneticButtons() {
    if (window.innerWidth < 992) return; // Desktop only

    const buttons = document.querySelectorAll('.btn-primary, .btn-secondary, .floating-cta');
    
    buttons.forEach(btn => {
        btn.addEventListener('mousemove', (e) => {
            const rect = btn.getBoundingClientRect();
            const x = e.clientX - rect.left - rect.width / 2;
            const y = e.clientY - rect.top - rect.height / 2;
            
            // Subtle magnetic pull
            btn.style.transform = `translate(${x * 0.3}px, ${y * 0.3}px) scale(1.05)`;
        });
        
        btn.addEventListener('mouseleave', () => {
            btn.style.transform = '';
        });
    });
}



import os

app_path = "c:\\Users\\Admin\\Documents\\dev\\ stuff\\Roofing\\js\\app.js"
app_path = "c:\\Users\\Admin\\Documents\\dev stuff\\Roofing\\js\\app.js"

form_js = """
/**
 * Contact Form Submission Handler
 */
document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('consultation-form');
    if (!form) return;

    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const btn = form.querySelector('button[type="submit"]');
        const originalText = btn.innerHTML;
        btn.innerHTML = 'Sending... <i class="fas fa-spinner fa-spin" style="margin-left: 10px;"></i>';
        btn.disabled = true;

        const formData = new FormData(form);
        const data = Object.fromEntries(formData.entries());
        
        // Handle multiple select
        const select = form.querySelector('#service-type');
        if (select) {
            data.services = Array.from(select.selectedOptions).map(opt => opt.value);
        }
        
        // Handle checkbox
        const checkbox = form.querySelector('input[name="insurance_claim"]');
        if (checkbox) {
            data.insurance_claim = checkbox.checked ? 'yes' : 'no';
        }

        try {
            const res = await fetch('/api/submit', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(data)
            });
            
            const result = await res.json();
            
            if (res.ok) {
                btn.innerHTML = 'Sent Successfully! <i class="fas fa-check" style="margin-left: 10px;"></i>';
                btn.style.background = '#10b981'; // green
                form.reset();
            } else {
                throw new Error(result.error || 'Failed to send');
            }
        } catch (error) {
            console.error('Error submitting form:', error);
            btn.innerHTML = 'Error. Try Again. <i class="fas fa-times" style="margin-left: 10px;"></i>';
            btn.style.background = '#ef4444'; // red
        }
        
        // Reset button after 3 seconds
        setTimeout(() => {
            btn.innerHTML = originalText;
            btn.disabled = false;
            btn.style.background = '';
        }, 3000);
    });
});
"""

with open(app_path, "a", encoding="utf-8") as f:
    f.write(form_js)

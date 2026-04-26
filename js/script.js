document.addEventListener('DOMContentLoaded', () => {
    // Intersection Observer for fade-in animations
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.1
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    const fadeElements = document.querySelectorAll('.fade-in');
    fadeElements.forEach(el => observer.observe(el));

    // Smooth Scrolling for navigation links
    document.querySelectorAll('a[href^="#"]:not([href="#"])').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            // e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });

    // Simple Form Handling
    const contactForm = document.getElementById('contact-form');
    if (contactForm) {
        contactForm.addEventListener('submit', (e) => {
            // e.preventDefault();
            const btn = contactForm.querySelector('button');
            const originalText = btn.textContent;

            btn.textContent = 'Sending...';
            btn.disabled = true;

            // Simulate sending
            /* setTimeout(() => {
                alert('Thank you for your message! I will be in touch shortly.');
                contactForm.reset();
                btn.textContent = originalText;
                btn.disabled = false;
            }, 1500); */
        });
    }
});


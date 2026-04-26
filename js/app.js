/* 
   BC Web Creator - Main Logic
*/

document.addEventListener('DOMContentLoaded', () => {
    initMobileMenu();
    initSmoothScroll();
    initIntersectionObserver();
    initShareButton();
});

// Mobile Menu Toggle
function initMobileMenu() {
    const toggle = document.querySelector('.mobile-toggle');
    const navLinks = document.querySelector('.nav-links');

    if (toggle && navLinks) {
        toggle.addEventListener('click', () => {
            navLinks.classList.toggle('active');

            // Optional: Animate hamburger icon
            const expanded = navLinks.classList.contains('active');
            toggle.setAttribute('aria-expanded', expanded);
        });

        // Close menu when clicking a link
        navLinks.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                navLinks.classList.remove('active');
            });
        });
    }
}

// Smooth Scrolling for Anchors
function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]:not([href="#"])').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;

            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                // Adjust for fixed header
                const headerOffset = 80;
                const elementPosition = targetElement.getBoundingClientRect().top;
                const offsetPosition = elementPosition + window.pageYOffset - headerOffset;

                window.scrollTo({
                    top: offsetPosition,
                    behavior: "smooth"
                });
            }
        });
    });
}

// Intersection Observer for Fade-in Animations
function initIntersectionObserver() {
    const fadeElements = document.querySelectorAll('.fade-in');

    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.1
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target); // Only animate once
            }
        });
    }, observerOptions);

    fadeElements.forEach(el => {
        observer.observe(el);
    });
}

// Share Button Logic
function initShareButton() {
    const shareBtn = document.getElementById('share-btn');
    if (!shareBtn) return;

    shareBtn.addEventListener('click', async () => {
        const shareData = {
            title: 'BC Web Creator',
            text: 'Professional web design and development for Vancouver businesses.',
            url: window.location.href
        };

        // Try Web Share API (Mobile/Modern Browsers)
        if (navigator.share) {
            try {
                await navigator.share(shareData);
            } catch (err) {
                console.log('Error sharing:', err);
            }
        } else {
            // Fallback: Copy to Clipboard
            try {
                await navigator.clipboard.writeText(window.location.href);

                // Show temporary "Copied!" feedback
                const originalText = shareBtn.innerHTML;
                shareBtn.innerHTML = '<span class="share-icon">✓</span> Copied!';
                shareBtn.style.backgroundColor = '#48bb78'; // Green success color

                setTimeout(() => {
                    shareBtn.innerHTML = originalText;
                    shareBtn.style.backgroundColor = '';
                }, 2000);
            } catch (err) {
                console.error('Failed to copy class', err);
            }
        }
    });
}

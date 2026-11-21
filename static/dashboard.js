/* Purpose: This file contains the JavaScript code for the dashboard page, handling dropdown menus, 
            search functionality, and navigation to the review submission page.
   Author: Cynthia Luizia */

// Profile and Feedback dropdown elements
const profileButton = document.getElementById('profileButton');
const feedbackButton = document.getElementById('feedbackButton');

const profileDropdown = document.getElementById('profileDropdown');
const feedbackDropdown = document.getElementById('feedbackDropdown');


// Function to toggle dropdown menus
function toggleDropdown(button, dropdown, otherButton, otherDropdown) {

    const willOpen = !dropdown.classList.contains('show');
    dropdown.classList.toggle('show', willOpen);
    button.setAttribute('aria-expanded', String(willOpen));
    // Close the other dropdown
    otherDropdown.classList.remove('show');
    otherButton.setAttribute('aria-expanded', 'false');
}

// Profile button 
profileButton.addEventListener('click', () => {
    toggleDropdown(
        profileButton,
        profileDropdown,
        feedbackButton,
        feedbackDropdown
    );
});

// Feedback button 
feedbackButton.addEventListener('click', () => {
    toggleDropdown(
        feedbackButton,
        feedbackDropdown,
        profileButton,
        profileDropdown
    );
});


// Close dropdowns when clicking outside
document.addEventListener('click', (event) => {
    if (!event.target.closest('.profile-area')) {
        profileDropdown.classList.remove('show');
        profileButton.setAttribute('aria-expanded', 'false');
    }
    if (!event.target.closest('.feedback-area')) {
        feedbackDropdown.classList.remove('show');
        feedbackButton.setAttribute('aria-expanded', 'false');
    }
});

// Search bar functionality
const searchInput = document.getElementById('reviewSearch');
const reviewCards = Array.from(
    document.querySelectorAll('.review-card')
);
const noResults = document.getElementById('noResults');
searchInput.addEventListener('input', () => {
    const query = searchInput.value.trim().toLowerCase();
    let visibleCount = 0;
    reviewCards.forEach(card => {
        const matches = card.dataset.search.includes(query);
        card.hidden = !matches;
        if (matches) {
            visibleCount++;
        }
    });
    noResults.style.display =
        reviewCards.length > 0 && visibleCount === 0
            ? 'block'
            : 'none';
});

// Navigate to the review submission page
document.querySelectorAll('[data-review-type]').forEach(button => {
    button.addEventListener('click', () => {
        const type = button.dataset.reviewType;
        const period = button.dataset.period;
        if (type === "open") {
            window.location.href =
                `/submit-reviews?period=${encodeURIComponent(period)}`;
        } else {
            alert("Confidential review submission is not available yet.");
        }
    });
});

/*
AI Disclosure:
Used ChatGPT as a learning resource to understand JavaScript event handling, DOM manipulation, interactive
elements, and assist with debugging.

Prompt Used:
"Can you explain how JavaScript event listeners, querySelectorAll, classList.toggle, and dataset attributes
work? Help me understand how to troubleshoot click events and connect HTML buttons to different webpages."
*/

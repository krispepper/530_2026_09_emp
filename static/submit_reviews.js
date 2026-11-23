/* Purpose: This JavaScript file handles the submission of performance reviews on the dashboard page. 
          It manages form submission, user feedback and validation.
   Author: Cynthia Luizia
*/  
const reviewForm = document.getElementById("reviewForm");
const reviewType = document.getElementById("reviewType");
const periodSelect = document.getElementById("periodID");
const privacyNote = document.getElementById("privacyNote");
const notice = document.getElementById("notice");
const statusInput = document.getElementById("status");
const submitButton = document.getElementById("submitButton");
const deleteButton = document.getElementById("deleteButton");

//Display a notice message to the user
function showNotice(message, type = "success") {
    notice.textContent = message;
    notice.className = `notice ${type === "success" ? "" : type}`;
    notice.hidden = false;
}

// Update the review type and privacy message 
function updateReviewType() {
    const selectedPeriod = periodSelect.options[periodSelect.selectedIndex];

    if (selectedPeriod && selectedPeriod.dataset.confidential === "true") {
        reviewType.value = "confidential";
    }

    const isConfidential = reviewType.value === "confidential";

    privacyNote.textContent = isConfidential
        ? "This is a confidential review. Your name will be hidden from the employee receiving the feedback."
        : "This is an open review and your name will be shown with this review.";

    submitButton.textContent = isConfidential
        ? "Submit confidential review"
        : "Submit open review";
}

//Listen for dropdown changes 
reviewType.addEventListener("change", updateReviewType);
periodSelect.addEventListener("change", updateReviewType);

//Handle the form submission
reviewForm.addEventListener("submit", async function (event) {
    event.preventDefault();
    if (!reviewForm.reportValidity()) {
        return;
    }

    const isConfidential = reviewType.value === "confidential";

    if (isConfidential) { 
        showNotice(
            "Confidential review form is ready, but it has not been saved.",
            "warning"
        );
        return;
    }

    statusInput.value = "Submitted";
    submitButton.disabled = true;
    submitButton.textContent = "Submitting...";

    try {
        const response = await fetch(reviewForm.action, {
            method: "POST",
            body: new FormData(reviewForm)
        });

        const message = await response.text();

        if (!response.ok) {
            throw new Error(message || "The review could not be submitted.");
        }

        showNotice(message || "Review was submitted.");
        statusInput.value = "Submitted";
        reviewForm.reset();
        updateReviewType();
    } catch (error) {
        statusInput.value = "In Progress";
        showNotice(
            error.message || "Unable to submit the review. Please try again.",
            "error"
        );
    } finally {
        submitButton.disabled = false;
        updateReviewType();
    }
});

//Handle the clear form button click
deleteButton.addEventListener("click", function () {
    const confirmed = window.confirm("Clear the information entered in this form?");
    if (!confirmed) return;

    reviewForm.reset();
    statusInput.value = "In Progress";
    showNotice("Form cleared.");
    updateReviewType();
});

updateReviewType();

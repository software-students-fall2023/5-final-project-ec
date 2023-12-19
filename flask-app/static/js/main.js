document.addEventListener("DOMContentLoaded", function() {
    const feedbackForm = document.getElementById('feedback-form');
    if (feedbackForm) {
        feedbackForm.addEventListener('submit', function(event) {
            const feedbackInput = document.getElementById('feedback');
            if (!feedbackInput.value.trim()) {
                alert('Please enter your feedback before submitting.');
                event.preventDefault(); // Prevent form from submitting
            } else {
                showConfirmation();
            }
        });
    }
});

function showConfirmation() {
    alert("Thank you for your feedback!");
}

document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    form.addEventListener('submit', function(event) {
        // Example of simple form validation
        const longUrlInput = document.getElementById('long_url');
        if (longUrlInput.value === '') {
            alert('Please enter a URL');
            event.preventDefault();
        }
    });
});

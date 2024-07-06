document.addEventListener('DOMContentLoaded', function() {
    // Function to show welcome message only on the first visit
    function showWelcomeMessage() {
        if (!sessionStorage.getItem('visited')) {
            alert("WELCOME TO MY TODO LIST");
            sessionStorage.setItem('visited', true);
        }
    }

    // Check for first visit when the page loads
    showWelcomeMessage();

    // Clear sessionStorage on page hide (when user navigates away)
    window.addEventListener('pagehide', function(event) {
        // Check if sessionStorage 'visited' is set and if it's not a button click
        if (sessionStorage.getItem('visited') && event.persisted) {
            sessionStorage.removeItem('visited'); // Remove 'visited' key
        }
    });
});



// AJAX request to submit form data
// fetch('/add', {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json',
//         },
//         body: JSON.stringify({ title: todoTitle }),
//     })
//     .then(response => response.json())
//     .then(data => {
//         console.log('Response:', data);
//         // Optionally handle response data (e.g., update UI)
//         // Example: Clear input field after successful submission
//         todoTitleInput.value = '';
//     })
//     .catch(error => {
//         console.error('Error:', error);
//         alert('Failed to add todo. Please try again.');
//     });
document.addEventListener("DOMContentLoaded", function() {
    // Function to set background based on URL
    function setBodyBackground() {
        const path = window.location.pathname;  // Get the current path
        const body = document.body;  // Get the body element
        
        if (path === "/") {
            body.style.backgroundImage = "url('/path/to/image1.jpg')";  // Set image1 if the URL is "/"
        } else {
            body.style.backgroundImage = "url('/path/to/image2.jpg')";  // Set image2 if the URL is not "/"
        }
    }

    // Initial check for background
    setBodyBackground();

    // Handle background change when URL changes in SPA
    window.onpopstate = function() {
        setBodyBackground();  // Re-check the URL when navigating back/forward
    };

    // You may need to hook into your SPA's navigation system
    document.querySelectorAll("a").forEach(link => {
        link.addEventListener("click", function(event) {
            event.preventDefault();
            history.pushState({}, "", this.href);  // Use history API to change the URL
            setBodyBackground();  // Update background after URL change
        });
    });
});


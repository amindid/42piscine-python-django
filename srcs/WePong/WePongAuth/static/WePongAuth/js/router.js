
document.addEventListener('DOMContentLoaded', function () {
    // Attach link listeners
    attachLinkListeners();

    // Function to fetch and load content
    function fetchPage(url) {
        fetch(url)
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.text();
            })
            .then(html => {
                const parser = new DOMParser();
                const doc = parser.parseFromString(html, 'text/html');
                const newContent = doc.querySelector('#root').innerHTML;
                
                // Update the content
                document.getElementById('root').innerHTML = newContent;
                
                // Update the URL
                history.pushState(null, '', url);
                
                // Reattach event listeners to new links
                attachLinkListeners();
            })
            .catch(error => console.error('Error loading page:', error));
    }

    function attachLinkListeners() {
        document.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', function (event) {
                event.preventDefault();
                const url = this.getAttribute('href');
                fetchPage(url);
            });
        });
    }

    // Handle back/forward navigation
    window.addEventListener('popstate', function () {
        fetchPage(window.location.pathname);
    });
});

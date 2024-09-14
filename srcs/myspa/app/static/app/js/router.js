document.addEventListener('DOMContentLoaded', function () {
    // Intercept link clicks
    document.querySelectorAll('a').forEach(link => {
        link.addEventListener('click', function (event) {
            event.preventDefault();
            const url = this.getAttribute('href');
            fetchPage(url);
        });
    });

    // Function to fetch and load content
    function fetchPage(url) {
        fetch(url)
            .then(response => response.text())
            .then(html => {
                const parser = new DOMParser();
                const doc = parser.parseFromString(html, 'text/html');
                const newContent = doc.querySelector('#root').innerHTML;
                document.getElementById('root').innerHTML = newContent;
                attachLinkListeners();  // Reattach event listeners to new links
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
});

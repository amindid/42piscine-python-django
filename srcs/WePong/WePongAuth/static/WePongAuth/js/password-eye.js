document.addEventListener("DOMContentLoaded", function() {
    const passwordInput = document.getElementById('password');
    const eyeIcon = document.getElementById('eye-icon');
    
    // Function to toggle password visibility
    eyeIcon.addEventListener('click', function() {
        const currentType = passwordInput.getAttribute('type');
        
        if (currentType === 'password') {
            // Change input type to text to show password
            passwordInput.setAttribute('type', 'text');
            // Update the icon (change to eye-slash.svg or other closed-eye icon)
            eyeIcon.src = "{% static 'WePongAuth/images/eye.svg' %}";
            eyeIcon.alt = "Hide password";
        } else {
            // Change input type back to password to hide it
            passwordInput.setAttribute('type', 'password');
            // Revert the icon back to the eye
            eyeIcon.src = "{% static 'WePongAuth/images/closed-eye.svg' %}";
            eyeIcon.alt = "Show password";
        }
    });
});

const togglePassword = document.querySelector('#togglePassword');
const password = document.querySelector('#password');
const lockIcon = document.querySelector('#lockIcon');

// Click event listener for both icons
lockIcon.addEventListener('click', toggleVisibility);
togglePassword.addEventListener('click', toggleVisibility);

function toggleVisibility() {
    // Toggle the type attribute
    const type = password.getAttribute('type') === 'password' ? 'text' : 'password';
    password.setAttribute('type', type);

    // Toggle the visibility of the icons
    togglePassword.style.display = togglePassword.style.display === 'none' ? 'inline-block' : 'none';
    lockIcon.style.display = lockIcon.style.display === 'none' ? 'inline-block' : 'none';
}

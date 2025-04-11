// Global phone number validation
document.addEventListener('DOMContentLoaded', function() {
    const contactNumberInput = document.getElementById('contact_number');
    if (contactNumberInput) {
        contactNumberInput.addEventListener('input', function() {
            const phoneNumber = contactNumberInput.value;
            const phoneNumberPattern = /^\d{10}$/;
            if (!phoneNumberPattern.test(phoneNumber)) {
                contactNumberInput.setCustomValidity('Please enter a valid 10-digit phone number');
            } else {
                contactNumberInput.setCustomValidity('');
            }
        });
    }
});
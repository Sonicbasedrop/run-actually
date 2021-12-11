/* Function for contact form to send email with 
    contact form contents to site owner */
function sendMail(contactForm) {
    emailjs.send("gmail","contact_form", {
        "from_name": contactForm.name.value,
        "from_email": contactForm.emailaddress.value,
        "comments": contactForm.comments.value

    })
    .then(
        function() {
            $('.response').html("Thank you for your message, have great day!");
        },
        function() {
            $('.response').html("There was an error with our email service. Please try again in a few minutes.");
        }
    );
    // Reset Form data
    document.getElementById("contact_form").reset();
    return false;
}
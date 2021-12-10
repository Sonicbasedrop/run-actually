// function for contact form to send email with contact form contents to site owner 
function sendMail(contactForm) {
    emailjs.send("service_mygcksp","contact_form", {
        "from_name": contactForm.name.value,
        "from_email": contactForm.email.value,
        "comments": contactForm.comments.value
    })
    .then(
        function() {
            $('.email-response').html("Thank you for your comment, we will get back to you ASAP.");
        },
        function() {
            $('.email-response').html("There was an error with our email service. Please try again in a few minutes.");
        }
    );
    // reset form data
    document.getElementById("contact-form").reset();
    return false;  
}


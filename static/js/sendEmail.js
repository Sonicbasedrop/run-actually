/* Function for contact form to send email with 
    contact form contents to site owner */
    function sendMail(contactForm) {
        emailjs.send("service_mygcksp","contact_form", {
            "from_name": contactForm.name.value,
            "from_email": contactForm.emailaddress.value,
            "comments": contactForm.comments.value
        })
        .then(
            function() {
                $('.emailaddress-response').html("Thank you for your email, someone will be in touch shortly.");
            },
            function() {
                $('.emailaddress-response').html("There was an error with our email service. Please try again in a few minutes.");
            }
        );
        // Reset Form data
        document.getElementById("contact-form").reset();
        return false;
    }
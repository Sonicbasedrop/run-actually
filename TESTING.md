![RUN||actually logo](readme_images/testing_images/color_palette_moc_logo/runsmlogo.png)
# RUN||actually - Testing

Back to my main README.md click [here](README.md)
<br>
The live site can be found [here](https://run-actually.herokuapp.com/)
<br>

**Table of Contents** 
1. [User Stories Testing](User-Stories-Testing)  
   - [Unregistered Users' Goals](Unregistered-Users-Goals)   
   - [Registered Users' Goals](Registered-Users-Goals)  
   - [Site Owners Goals](Site-Owners-Goals)    
2. [Manual Testing](Manual-Testing)
   - [Issues and Resolutions](Issues-and-Resolutions) 
   - [Crud Functinality](Crud-Functionality)  
   - [Browser Compatibility](Browser-Compatibility)   
   - [Devices](Devices)   
   - [Responsiveness](Responsiveness)   
   - [Links](Links)  
   - [Forms](Forms)   
   - [Defensive Testing](Defensive-Testing)  
4. [W3C Validator Testing](W3C-Validator-Testing)  
   - [HTML](HTML)   
   - [CSS](CSS)  
5. [JSHint Testing](JSHint-Testing)    
6. [Pep8 Testing](Pep8-Testing)
7. [Lighthouse Testing](Lighthouse-Testing)  

## **1. User Stories Testing**  
### **Unregistered User Goals**   
As a new/ unregistered user, I want to:
1. Be able to search for an event easily
   * As a user, I want the main purpose of the site to be clear so that I immediately know what the site is intended for upon entering.   
   * As a user, I want to easily navigate the site so that I can find content quickly with ease.<br>
   ![Clear information on landing page](readme_images/testing_images/user_stories_images/index_page.png)<br>
   * As a user, I want the website to be responsive so that I can clearly view the webpages from my mobile, tablet or desktop.<br>
   ![](readme_images/testing_images/user_stories_images/user_mockup.png)
   <br>
   
   2. Signup
    * As a user, I want to be able to register to the website so that I can create and manage my own events.
   <br>
   ![Sign up page](readme_images/testing_images/user_stories_images/signup_sucssess.png)  

3. Explore all events.  
   * As a user, I want to be able to search or filter events based on custom criteria so that I can find events  
  <br>
  ![Search for events](readme_images/testing_images/user_stories_images/evnents_page_1.png)

4. * As a user, I want a way to contact the site owner so i case have any questions regarding
the website or upcoming races and receive feedback to alert on form submission.
   <br>
  ![Contact](readme_images/testing_images/user_stories_images/contact_page.png)

5. Navigate intuitively and can see the Sign-Up button right away  
   * For unregistered users, the links on Navbar that are available to navigate are: Home, Events,Sign Up, and Log In. The footer is also avalible to a unregistered users, the links in footer that is avalible to all users are: About and Contact. 
   <br>
  ![About](readme_images/testing_images/user_stories_images/about_page.png)
    <br>
  * As a user, I want to be able to return to the main site without having to use the browser buttons so that I can easily return to the website if I navigate to a page that doesn't exist. 
 <br>
  ![404 page not found](readme_images/testing_images/user_stories_images/404_page.png)
  <br>
  ### **Registered User Goals**   
1. Understand what the site is about and how it works  
  * On the Profile page, inside the hero-image, a page title website are placed between the navbar and the profile card, and short welcome introduction to the website with a insperational message.
 
2. See all events 
   * On the Events Page, the user can search for all avalible events in the datbase.
   and a signed up user have the ability to create events.
  <br>
  ![Events](readme_images/testing_images/user_stories_images/events_page.png)

3. Create events
 * Once logged user have created an event, the user have the ability to to Edit or Delete   said event. 
<br>
  ![Create event](readme_images/testing_images/user_stories_images/evnents_page_1.png)
<br>
4. Delete events
   * If a user decides to delete an event a modal will appear and ask user if user is are sure they want to delete the event. Only then can the user delete the event.
<br>
![Delete an event](readme_images/testing_images/user_stories_images/delete_event.png)


### **Site Owners Goals**
As Site owner/Admin user, I want to:
1. Be able to create,edit and delete events.
   * All functions as a general user are available for the admin.
   <br>
   ![Delete an event](readme_images/testing_images/user_stories_images/delete_event.png)
   <br>
    * To increase the number of participants in runners events by providing a simple, easy to use website that
contains all the details of upcoming events.
<br>
   * Charities play a vital role in our lives and communities and Charities rely on fundraising to keep doing their work. Taking on a challenge is the perfect opportunity to start fundraising. This site give organizations and/or indivduals the opportunity to create charity runns so support great causes.
<br>
   * Maintaining good health doesn't happen by accident. It requires work, smart lifestyle choices and Physical exercise. Exercise is important for people with mental illness ??? it not only boosts our mood, concentration and alertness, but improves our cardiovascular and overall physical health. This site is all about promoting a healther way of life.
<br>

2. Add, Edit, and Delete categories   
   * Once the Site owner/Admin is logged in, a "Manage Categories" button will be visible in the navbar.
   <br>
   ![Manage-Categories](readme_images/testing_images/user_stories_images/categories_page.png)
  <br>

  ## **3. Manual Testing by the developer** 

### **Issues and Resolutions**
- I hade som issues with the editing function i Python, I contacted tutor support and was informed that the "update()" inwas deprecated and "udate_one()" in in conjunction with       "{"$set": submit})" and it did work.

- I also hade a issue with delete functionality in Python, I found the sulotion on W3Shools.
"remove()" had been deprecated and "delete_one()" works fine.

### **Crud Functionality** 
- The four functions that are considered necessary to implement a persistent storage application: create, read, update and delete. All functions works correctly.

### **Browsers Compatibility**  
- The website was tested using the following browsers: Google Chrome,, Opera, Mozilla Firefox, and Safari.  

### **Devices**
The website was also viewed on the following devices: 
- Mac laptop
- Windows Laptop  
- Tablets: iPad Mini 2 and iPad Pro
- Mobile: iPhone7, iPhone 8, iPhone 4,  
- Family members review the site on their devices and did any experience issues.  

 ### **Responsiveness**
- To check the responsiveness of the website across all devices, the developer tools was used regularly during the developing process. 

### **Links**  
The links were tested to ensure that:  
- All navigation links are linking correctly.  
- All input fields and the buttons are functioning as expected 
- The social media links are working and opening in a new tab.  

### **Forms**
**The form was also tested to ensure that:**  
- The required attributes are working.  
- The regex patterns for username and password are working as expected.
- The user will be promted if the user uses the rong format when filling out form.  
- If a user uses the rong format, the site will not brake.

**For Contact Form test was performed to ensure that:**  
- When a valid Contact form is submitted, a message appear between the textarea and submitbutton "Thank you for your message, have a great day" as a response to the user.  
- The Contact Form is reset and all fields are empty.  
- The developer gets the notification message in their inbox. 
<br>

## **4. W3C Validator Testing**  
The [W3C Markup Validator Sevice](https://validator.w3.org/) and [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) were used to validate the website to ensure there were no syntax errors. No error was found: 

### **HTML**
 !|[Homepage](readme_images/testing_images/w3c_validator/html/index.png) 
 <br>
 !|[Signup](readme_images/testing_images/w3c_validator/html/signup.png)
 <br>
 !| [Login](readme_images/testing_images/w3c_validator/html/login.png)
 <br>
 !| [About](readme_images/testing_images/w3c_validator/html/about.png)
 <br>
 !| [Contact](readme_images/testing_images/w3c_validator/html/contact.png) 
 <br>
 !|[Events](readme_images/testing_images/w3c_validator/html/events.png)
 <br>
 !|[Create Event](readme_images/testing_images/w3c_validator/html/create_event.png)
 <br>
 !|[Categories](readme_images/testing_images/w3c_validator/html/categories.png)
 <br>
 !|[Create Category](readme_images/testing_images/w3c_validator/html/create_category.png)
 <br>
 
### **CSS**
!|[CSS](readme_images/testing_images/w3c_validator/css/css_validation.png)
<br>
## **5. JavaScript Testing**  
The javascript code through [JSHint](https://jshint.com/), and there were some warnings, but no errors.
<br>
!|[EmailJS](readme_images/testing_images/jshint/sendEmailjs.png)
<br>
!|[jQuery for MaterializeCSS](readme_images/testing_images/jshint/Materializejs.png)
<br>
!|[Get current year JS](readme_images/testing_images/jshint/fullYear.png)
<br>
## **6. Pep8 Online Testing**
The python code through was ran true [Pep8 Online](http://pep8online.com/) no errors found.
<br>
!|[Python code](readme_images/testing_images/pep_8/pep8.png)
<br>
## **7. Lighthouse Testing**  
The Chrome Lighthouse testing was used to audit the performance, accessibility, best practices, and SEO. Below are the results.
<br>
!|[Homepage Mobile](readme_images/testing_images/lighthouse/index_mobile.png)
<br>
!|[Homepage Desktop](readme_images/testing_images/lighthouse/index_desktop.png)
<br>
!|[About Mobile](readme_images/testing_images/lighthouse/about_mobile.png)
<br>
!|[About Desktop](readme_images/testing_images/lighthouse/about_desktop.png)
<br>
!|[Categories Mobile](readme_images/testing_images/lighthouse/categories_mobile.png)
<br>
!|[Categories Desktop](readme_images/testing_images/lighthouse/categories_desktop.png)
<br>
!|[Contact Mobile](readme_images/testing_images/lighthouse/contact_mobile.png)
<br>
!|[Contact Desktop](readme_images/testing_images/lighthouse/contact_desktop.png)
<br>
!|[Create Category Mobile](readme_images/testing_images/lighthouse/create_category_mobile.png)
<br>
!|[Create Category Desktop](readme_images/testing_images/lighthouse/create_category_desktop.png)
<br>
!|[Create Event Mobile](readme_images/testing_images/lighthouse/create_event_mobile.png)
<br>
!|[Create Event Desktop](readme_images/testing_images/lighthouse/create_event_desktop.png)
<br>
!|[Events Mobile](readme_images/testing_images/lighthouse/events_mobile.png)
<br>
!|[Events Desktop](readme_images/testing_images/lighthouse/events_desktop.png)
<br>
!|[Login Mobile](readme_images/testing_images/lighthouse/login_mobile.png)
<br>
!|[Login Desktop](readme_images/testing_images/lighthouse/login_desktop.png)
<br>
!|[Profile Mobile](readme_images/testing_images/lighthouse/profile_mobile.png)
<br>
!|[Profile Desktop](readme_images/testing_images/lighthouse/profile_desktop.png)
<br>
!|[Signup Mobile](readme_images/testing_images/lighthouse/signup_mobile.png)
<br>
!|[Signup Desktop](readme_images/testing_images/lighthouse/signup_desktop.png)

* [Back to top of page](https://github.com/Sonicbasedrop/run-actually/blob/main/TESTING.md)



 
 
 





   
 


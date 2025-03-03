# Persian Foods

Persian Foods is a full-stack web application designed to provide users with a platform to explore, share, and interact with a wide variety of recipes. The website’s goal is to offer a simple, intuitive, visually appealing, and user-friendly space where users can discover recipes shared by food enthusiasts from all over the world, contribute their own recipes, and engage with the community. The target audience is anyone with a passion for cooking and a curiosity about world cuisines, ranging from young adults to older generations.

- The interactive platform incorporates user authentication and full CRUD functionality, allowing users to create, read, update, and delete recipes stored in a relational database. In addition, users can search for recipes, like their favorites, and interact with other community members through comments.
- The Persian Foods website also includes an admin dashboard, enabling administrators to review and approve user comments and manage recipe content.

- The website is built using HTML, CSS, JavaScript, Python, and the Django framework as part of Portfolio Project #4 for the Code Institute’s Full Stack Software Development course.

![persian-foods-mockup-image](documentation/images/mockup/mockup.png)


### [Link to Live Website](https://django-persian-foods-c85134c12b3e.herokuapp.com/)

------

## Table of Contents

 - [Persian Foods](#persian-foods)
   - [Table of Contents](#table-of-contents)
 - [User Experience Design](#user-experience-design)
   - [The Strategy Plane](#the-strategy-plane)
    - [Site Goals](#site-goals)
    - [Agile planning](#agile-planning)
      - [Milestones](#milestones)
      - [User Stories](#user-stories)
   - [The Structure Plane](#the-structure-plane)
      - [Features](#features)
      - [Features Left to Implement](#features-left-to-implement)
   - [The Skeleton Plane](#the-skeleton-plane)
    - [Wireframes](#wireframes)
      - [Desktop Wireframes](#desktop-wireframes)
      - [Mobile Wireframes](#mobile-wireframes)
    - [Database Design](#database-design)
   - [The Surface Plane](#the-surface-plane)
    - [Design](#design)
 - [Technologies](#technologies)
   - [Tools and Technologies](#tools-and-technologies)
   - [Imports](#imports)
    - [Python Packages](#internal-packages)
    - [External Packages](#external-packages)
 - [Testing](#testing)
  - [Responsiveness](#responsiveness)
  - [Accessibility](#accessibility)
  - [Lighthouse](#lighthouse)
  - [Validator Testing](#validator-testing)
    - [HTML Validation](#html-validation)
    - [CSS Validation](#css-validation)
    - [JavaScript Validation](#javascript-validation)
    - [Python Validation](#python-validation)
  - [Manual Testing](#manual-testing)
    - [Functional testing](#functional-testing)
    - [Links and Buttons](#links-and-buttons)
    - [Negative Testing](#neagtive-testing)
  - [Automated Testing](#automated-testing)
    - [Unit Tests](#unit-tests)
 - [Bugs](#bugs)
 - [Deployment](#deployment)
   - [Version Control](#version-control)
   - [Deployment In Heroku](#deployment-in-heroku)
   - [Cloning the Repository](#cloning-the-repository)
   - [Forking](#forking)
 - [Credits](#credits)
 - [Acknowledgements](#acknowledgements)


# User Experience Design

## The Strategy Plane

### Site Goals

The website is designed for everyone who loves cooking and exploring cuisines from around the world, with a special focus on Persian foods. It also caters to those searching for inspiration on days when they want to try something new and discover diverse recipes. The application offers a vibrant and engaging platform for food enthusiasts to explore, share, and indulge in culinary delights, especially from Persian traditions.

Through a user-friendly interface, users can discover a wide range of recipes tailored to their tastes and love for various cuisines.

 - The site allows users to share their favorite recipes, exchange cooking tips, and connect with like-minded food lovers who share a passion for Persian cuisine.
 - Featuring a visually appealing, clean, and earthy design, the site aims to inspire and delight users, whether they are browsing on a desktop or mobile device.


### Agile Planning

I employed the Agile methodology and utilized a GitHub project board to organize and develop my user stories starting from the project planning stage and continuing until the final product was built. To enhance clarity and structure, a user story template is designed that precisely outlines each user story with an acceptance criteria to be fulfilled. Small features have been assigned to 7 milestones.

- All User Stories include:
   - Acceptance Criteria
   - Labels (MoSCoW Prioritization)
- Labels have been used to mark which features the project : 'must have', 'should have', 'could have' and 'nice to have'. The prioritization was done so that a MVP for the project is created in time I have and only focus on the 'should haves' or 'could haves' if the time allows.
- Each User story was checked for the acceptance criteria have been met and closed.

- The detailed Project Board with all user stories can be found here.[Project Board Link](https://github.com/Naviid24/persian-foods-pp4/projects?query=is%3Aopen)

<details><summary>Issues List</summary>


![issues](documentation/images/gile/issues_list.png)

</details>

<details><summary>Project Board</summary>


![project board](documentation/images/gile/project_board.png)

</details>

#### Milestones

- **1 - Initial Project Setup:**
  The first task in starting the project was to setup it up. All the tasks from setting up github repository to installing django, setting up django app and related packages and libraries were included in this milestone. The acceptance criteria was refined for each of the setup to be completed for clarity and ease of understanding. 

- **2 - User Authentication:**
This milestone covers user authentication and authorization i.e. user sign-up, sign-in and logout so that user can explore complete features and functionality of the website.

- **3 - Post Functions:**
All the CRUD functionality and features related to recipes (comments, likes) is included here.

- **4 - User Interface Design (UX/UI):**
The website to be user-friendly and responsive on all devices, this milestone covers the styling aspects of the site, from website pagination to responsiveness and error pages so that user has smooth experience throughout the application.

- **5 - Admin Functionality:** 
Includes admin dashboard functionality so that admin can monitor the website for users, recipes and comments. This milestone was included to keep the admin and site user functionality separate for clarity. 

- **6 - Project Documentation:**
This milestone was needed so that I can document my project in-depth with all website features, testing, deployment information.

- **7 - Final Project Deployment:**
Included as it was absolutely necessary and important to have a live link of fully functional website with no errors so that everyone can have access to the application.

#### User Stories

Each Milestone covers the user stories for small features allowing me to prioritize the most important ones to least in project development.

- **Milestone 1 - Initial Project Setup:**
    - As a developer, I need to set up the recipe blog project with all the necessary components and configurations so that I can ensure a smooth development and deployment process.
       - Initialize and setup a GitHub repository with a README file using CI Gitpod template.
       - Install the latest version of Django.
       - Create a new Django project.
       - Add main app.
       - Verify that the project runs without errors using the Django development server.
       - Add a requirements.txt file listing all project dependencies.
       - Add env.py file to store sensitive information.
       - Add Procfile
       - Implement a proper media storage configuration for user-uploaded images.
            - image database: Cloudinary
       - Configure the project to use a PostgreSQL database.
       - Update the settings.py file to notify Django of the installed supporting libraries .
       - Deploy project to Heroku to test deployment is successful.

    - As a developer, I need to create a base.html file so that I can have a basic structure of the page for the project.
    - As a developer, I need to add static files and media so that I can build the website to be user friendly, interesting and responsive to all screen sizes.
    - As a developer, I need to create a navigation menu so that a website user can easily navigate through the site pages and content.
       - Home Page - for all users
       - Browse Recipes Page - for all users
       - Signup Page - for unauthorised user's registration
       - Login Page - for users already registered
       - Logout Page - for authorised users
       - User Drafts Recipe Page - for authorised users
       - Create new recipes Page - for authorised users
    - As a developer, I need to create a footer so that I can include social media links, contact links and relevant site information about the website.

- **Milestone 2 - User Authentication:**
    - As a developer, I need to setup allauth so that users can have an option to register and sign-in to the website for exploring more features.
      - Install allauth
      - Implement register, login and logout functionality
      - Verify that users can register/ login and logout of their account with an appropriate message displayed.
    - As a Site User I can register an account so that I can access publishing, commenting and like/unlike features.

- **Milestone 3 - Recipe Post Functions:**
   - As a logged-in User, I can create/publish recipes so that I can share recipes that I find delicious with others.
   - As a logged-in User, I can edit the recipes that I have shared so that I can correct and update the recipe details if necessary.
   - As a logged-in User, I can delete my recipes so that they are no longer published on the site.
   - As a Site User, I can view and read the detailed recipes shared/published by others so that I can get some inspiration.
   - As a Site User, I can view a paginated list of recipe posts so that I can select which recipes I want to view.
   - As a logged-in User, I can go to a page to view only my recipes so that I can easily access them if needed.
   - As a Site User, I can search recipes so that I can only view recipes I am interested in.
   - As a Site User, I can leave comments on recipes so that I can interact with others/share my opinion.
   - As a Site User, I can view comments on an individual recipe post so that I can read the conversation.
   - As a logged-in User, I can like/unlike others' recipes so that I can interact with the content.

- **Milestone 4 - User Interface Design (UX/UI):**
    - As a developer, I need to create a home page so that the user can quickly understand what the recipe blog offers and navigate easily to find interesting recipes.
    - As a User, I can navigate between pages easily, so that I can explore the website content without any chaos.
    - As a developer, I want to style the allauth authentication pages(signup, login and logout pages) so that they are visually consistent with the rest of the website and provide a seamless user experience.
    - As a Site User, I can get corresponding feedback after taking an action so that I know whether my actions were successfully run or not.
    - As a User, I want to be directed to a 403 error page when attempting to access content or functionality that I am not authorized to view, so that I am aware of my access limitations and can take appropriate action.
    - As a User, I want to be directed to a custom 404 page when I navigate to a broken link or URL that does not exist, so that I am informed that the page I am looking for is not available and can be directed to other relevant sections of the website.
    - As a user, I am notified in case of an internal error so that I can understand what went wrong and how to proceed.

- **Milestone 5 - Admin Functionality:** 
   - As a developer, I need to create a superuser so that I can manage the website efficiently and ensure the quality and organization of content on the website.
   - As a Site Admin I can create, read, update and delete recipe posts so that I can manage my recipe blog content.
   - As a Site Admin I can approve or disapprove comments so that I can filter out objectionable comments.

- **Milestone 6 - Project Documentation:**
   - As a developer, I need to create readme.md file so that the project is documented in detail.

- **Milestone 7 - Final Project Deployment:**
   - As a developer, I need to make sure the project is deployed to heroku so that everything works and looks as expected.

## The Structure Plane

### Features

### Existing Features

#### Navigation Menu

- As a developer, I need to create a navigation menu so that a website user can easily navigate through the site pages and content. **(User Story#4) (must have)**
- As a User, I can navigate between pages easily, so that I can explore the website content without any chaos. **(User Story#22) (should have)**

##### Navigation bar for all users
![navigation-bar-view](documentation/images/feutures/nav-bar-all-user.png)

##### Navigation bar for authorised users
![navigation-bar-view](documentation/images/feutures/navbar-authenticated-user.png)

- The navigation bar is shown on all pages based on the users logged-in(authentication) status and is responsive to all screen sizes. For smaller screen sizes the navigation bar appears as a compact menu and can be easily accessed. A success message is displayed when user is logged-in/ registered.
- The design is kept clean and simple so that user can navigate between the pages easily without any confusion. The links are visible clearly both on large screen and smaller screen sizes. 
- The active link is marked for ease of accessibility so that the user knows the current page been visited.
- The navigation menu includes:
    - Home Page - for all users
    - Recipes Page - for all users
    - Sign up Page - for unauthorised user's registration
    - Sign in Page - for users already registered
    - Logout Page - for authorised users

#### Home Page

- As a developer, I need to create a home page so that the user can quickly understand what the recipe blog offers and navigate easily to find interesting recipes. **(User Story#21) (must have)**

![home-page-for-authenticated-user](documentation/images/feutures/home-authenticated.png)

![home-page-for-all-user](documentation/images/feutures/home-all-users.png)

#### Footer

- As a developer, I need to create a footer so that I can include social media links, contact links and relevant site information about the website. **(User Story#5) (must have)**

![footer-section-view](documentation/images/feutures/footer.png)

- The footer section includes the information about the website: the developer of the website, the purpose (for educational purpose only), year developed and the developer's GitHub and LinkedIn links.
- Similar to the navigation bar, the footer is displayed on every page of the website. It displays icon links to GitHub and LinkedIn accounts. These icon links can enable user to see more about my work through GitHub and learn more about me through LinkedIn. Both the links opens in new page.

#### Sign-Up / Sign-In / Logout Pages

- As a developer, I need to setup allauth so that users can have an option to register and sign-in to the website for exploring more features. **(User Story#6) (must have)**

- As a Site User I can register an account so that I can access publishing, commenting and like/unlike features. **(User Story#7) (must have)**

- As a developer, I want to style the allauth authentication pages(signup, login and logout pages) so that they are visually consistent with the rest of the website and provide a seamless user experience.
**(User Story#23) (should have)**

![sign-up-page](documentation/images/feutures/signup.png)

![sign-in-page](documentation/images/feutures/sign-in.png)

![sign-out-page](documentation/images/feutures/sign-out.png)

- All the pages are accessible from navigation bar for large and small screen sizes.
- User can easily access the sign-up / sign-in options to explore the website features completely.
- A clear message is displayed on the pages for user to know whether he needs to sign-in or sign-up to explore the recipe website and to like, comment and post the recipes.
- A success message is displayed to user based on his actions for sign-in, sign-up and sign-out.

#### Add Post

- As a logged-in User, I can create/publish posts so that I can share food posts that I find delicious with others. **(User Story#8) (must have)**

![add-post-view](documentation/images/feutures/add-post.png)

- CRUD Functionality - The Add Recipe page link is only visible and accessible to logged-in users. On clicking the Add post link, authorised users are directed to the create post form. The form field marked as * are mandatory to be filled. If user tries to submit the form without entering all required field, messages are displayed below relevant fields that are left empty.
- A default image is incorporated so that if the user is unable to provide any recipe image, the default image will act as one.
- All the fields in the form except the Recipe Image field are required. The form is not deemed to be valid in case any of the fields are left empty. User can either publish or save recipe as draft. 
- Users can share their recipes with others using the add recipe form. On submitting the recipe, user is displayed with a success message and directed to the Recipes page.


#### Edit Post

- As a logged-in User, I can edit the recipes that I have shared so that I can correct and update the recipe details if necessary. **(User Story#9) (must have)**

![edit-post-button](documentation/images/feutures/edit-post.png)

![edit-post-page-view](documentation/images/feutures/edit-post.png)

- CRUD Functionality - the feature of edit in post details page is only visible and accessible to the logged-in users and only if the user is the author of the post.
- On clicking the edit button user is directed to the Edit post form/page where user can update / edit post for any changes and can either save as draft or publish it. On successful update of the post, user is displayed with success message and directed to Posts Page.
- If unauthorised user accesses the link the 403 error page will be displayed.

#### Delete Post

- As a logged-in User, I can delete my posts so that they are no longer published on the site. **(User Story#10) (must have)**

![delete-button-view](documentation/images/feutures/edit-post-button.png)

![delete-post-page-view](documentation/images/feutures/delete-post-confirmation.png)


- CRUD Functionality - the feature of delete in post details page is only visible and accessible to the logged-in users and only if the user is the author of the post.
- User is directed to confirm delete page where user can either delete the post or cancel. 
- The post is permanently deleted if delete is confirmed and a success message is diplayed to user else user will be taken back to post details page if cancelled.
- If unauthorised user accesses the link the 403 error page will be displayed.

#### Edit Comments

- As a logged-in User, I can edit the Posts that I have shared so that I can correct and update the recipe details if necessary. **(User Story#9) (must have)**

![edit-comment]()



#### Delete Posts

- As a logged-in User, I can delete my recipes so that they are no longer published on the site. **(User Story#10) (must have)**

![delete-post](documentation/doc-images/delete-comment.png)

- CRUD Functionality - the feature of delete in recipe details page is only visible and accessible to the logged-in users and only if the user is the author of the recipe.
- User is directed to confirm delete page where user can either delete the recipe or cancel. 
- The recipe is permanently deleted if delete is confirmed and a success message is diplayed to user else user will be taken back to recipe details page if cancelled.
- If anauthorised user accesses the link the 403 error page will be displayed.


#### Post Details

- As a Site User, I can view and read the detailed posts shared/published by others so that I can get some inspiration. **(User Story#11) (must have)**

##### Post Details View for authorised users
![post-details-page](documentation/images/feutures/post-detail.png)

- User can view a detailed post on this page along with number of comments, number of likes and the all post information.
- The edit and delete buttons are visible and accessible only to the logged-in user as author of the post.
- Logged-in users can explore the post details page completely for like / unlike and comments feature.

##### Post Details View for Logged-in User and author of the post

![post-details-page](documentation/images/feutures/post-detail-author.png)

#### Posts Pagination (Posts Page)

- As a Site User, I can view a paginated list of posts so that I can select which posts I want to view. **(User Story#12) (should have)**

![posts-pagination](documentation/images/feutures/pagination.png)

- This feature allows posts to be paginated by 4 posts per page, given more than 1 page the next and prev buttons appear adjacent to each other.
- The posts list page is kept simple so that it is not overcrowded and user can find it easy to navigate between the pages.
- On clicking the Read more button user is taken to post details page to view complete post information.

#### My Drafts Page

- As a logged-in User, I can go to a page to view only my recipes so that I can easily access them if needed.
**(User Story#13) (should have)**

- **Note:** The user story is partially complete. User can only view the posts saved as draft in my drafts page for now. User can update the draft post from my drafts page to either publish or save it for later. 
- This page is only accessible and visible to logged-in users.
- The paginated list of post drafts is displayed with 4 posts per page (if present). With this feature user can create post and save for later as draft for changes or to publish later.
- User can also make his published posts draft for any changes. This feature allows a flexibility for user to share posts and manage them.

![my-drafts-recipe-view](documentation/images/feutures/draft.png)


#### Search posts Page

- As a Site User, I can search posts so that I can only view posts I am interested in. **(User Story#14) (could have)**

![search-posts-page](documentation/images/feutures/search.png)

![search-results-page](documentation/images/feutures/search-result.png)

![search-not-found-page](documentation/images/feutures/search-not-found.png)

- The search post page allows users to search posts by title or keyword. This page is accessible throughout the website and to all users.
- If the user search results are not found, a message for refining search is provided. Also user is encouraged to share own posts or view all posts.
- If search query is not provided by user, the page is loaded with message to search bu post title or keyword.


#### Comment Section

- As a Site User, I can leave comments on posts so that I can interact with others/share my opinion. **(User Story#15) (should have)**

- As a Site User, I can view comments on an individual post so that I can read the conversation. **(User Story#16) (should have)**

##### Comments Section for author of the comment
![comment-view-](documentation/images/feutures/coment-management.png)

##### Comments Section for all logged-in users
![comment-view-loggedin-users](documentation/images/feutures/comment-login-users.png)


#### Like / Unlike Post

- As a logged-in User, I can like/unlike others' posts so that I can interact with the content. **(User Story#17) (should have)**

![liked-post-view](documentation/images/feutures/like.png)
![liked-post-view](documentation/images/feutures/unlike.png)

- The like / unlike feature allows logged-in user to like or unlike the posts.
- Authorised user - likes the posts (if didn't previously liked the post), thumb icon will be displayed - if clicked the icon will change to solid blue color and the number of likes will increase by one.
- Authorised user - unlikes the post (if previously liked the post) , the number of likes will be decreased by one.

#### Admin Functionality

- As a developer, I need to create a superuser so that I can manage the website efficiently and ensure the quality and organization of content on the website. **(User Story#24) (must have)** 
- As a Site Admin I can create, read, update and delete recipe posts so that I can manage my recipe blog content. **(User Story#25) (must have)**
- As a Site Admin I can approve or disapprove comments so that I can filter out objectionable comments. **(User Story#26) (must have)**

![admin-functionality-view](documentation/images/feutures/admin.png)

- The most important task for website to function was to create a superuser, to manage the recipe post functionality and the website entirely.
- The admin can ensure the quality and organization of the content on the webite.
- When the comment is made by any user on the post, the comment awaiting approval message is displayed to user. The comment is only displayed if it approved by admin.
- The admin panel helps the administrator to have control over the website to function seamlessely and keep the website content meaningful and organized.

#### Feedback on user actions

- As a Site User, I can get corresponding feedback after taking an action so that I know whether my actions were successfully run or not. **(User Story#18) (must have)**

![user-signin-success-message](documentation/images/feutures/signed-in-feedback.png)

![user-signed-out](documentation/images/feutures/signed-out-feedback.png)

- This feature informs the user if the action taken has been successful so that user can know the outcome of every action throughout while navigating the website.
- Message will be displayed when :
    - User Sign In / Sign Up / Logout
    - User posted a recipe
    - User edited the recipe
    - User deleted the recipe
    - User comments on a recipe



#### Error Pages

- As a User, I want to be directed to a 403 error page when attempting to access content or functionality that I am not authorized to view, so that I am aware of my access limitations and can take appropriate action.
**(User Story#27) (must have)**
- As a User, I want to be directed to a custom 404 page when I navigate to a broken link or URL that does not exist, so that I am informed that the page I am looking for is not available and can be directed to other relevant sections of the website. **(User Story#28) (should have)**

- As a user, I am notified in case of an internal error so that I can understand what went wrong and how to proceed. **(User Story#29) (nice to have)**

![error-404-page](documentation/images/feutures/404-error.png)
![error-500-page](documentation/images/feutures/500-error.png)

- The custom error pages are displayed if user encounters an error while accessing unauthorised link(access denied), user navigates to a page not present(page not found), or if there is internal error while rendering the user requested resource.
- This feature communicates to the user about what went wrong and gives option to go back to the home page. This gives user an option to navigate the website again without leaving it.
- The message displayed for each of the error is user-friendly and gives user an easy to access option to go back to home page through providing the home page link.


#### Initial Project Setup / Project Documentation / Final Project Deployment
All the user stories are completed for project setup, project documentation and final project deployment

- As a developer, I need to set up the Persian Foods blog project with all the necessary components and 
  configurations so that I can ensure a smooth development and deployment process. **(User Story#1) (must have)**
    - Initialize and setup a GitHub repository with a README file using CI Gitpod template.
    - Install the latest version of Django.
    - Create a new Django project.
    - Add main app.
    - Verify that the project runs without errors using the Django development server.
    - Add a requirements.txt file listing all project dependencies.
    - Add env.py file to store sensitive information.
    - Add Procfile
    - Implement a proper media storage configuration for user-uploaded images.
            - image database: Cloudinary
    - Configure the project to use a PostgreSQL database.
    - Update the settings.py file to notify Django of the installed supporting libraries .
    - Deploy project to Heroku to test deployment is successful.

- As a developer, I need to create a base.html file so that I can have a basic structure of the page for the project. **(User Story#2) (must have)**
- As a developer, I need to add static files and media so that I can build the website to be user friendly, interesting and responsive to all screen sizes. **(User Story#3) (must have)**
- As a developer, I need to create Readme.md file so that the project is documented in detail. **(User Story#19) (must have)**
- As a developer, I need to make sure the project is deployed to heroku so that everything works and looks as expected. **(User Story#20) (must have)**

### Features left to implement

- Implement a customizable User profile section where user can add personal information (profile picture / avatar, bio, interests, favourite recipes) and view his published and draft recipes (currently user can view only draft recipes in my drafts page).
- Add a feature that allows users to click on the author's name and view all the Posts published by that author.
- Add a search page to search all posts of the blog
- Enhance search functionality to search for recipes based on FuzzySearch.
- Provide users with social media options to login.
- Add a subscription feature so that user can get latest posts through email.
- Add a feature on an individual profile to follow eachother

## The Skeleton Plane

#### Desktop Wireframes
Wireframes for Large Screen Sizes 

#### Home Page 
![home-page-desktop-wireframe](documentation/images/wireframes/desctop-wireframes/home-unauth-wireframe.png)

#### Posts List page
This page is accessible for just logged-in users
![posts-list-desktop-wireframe](documentation/images/wireframes/desctop-wireframes/posts-list-wireframe.png)

#### Add Posts page
![add-post-desktop-wireframe](documentation/images/wireframes/desctop-wireframes/add-post-wireframe.png)

#### Search Posts page
![search-post-desktop-wireframe](documentation/images/wireframes/desctop-wireframes/search-wireframe.png)

#### My Drafts page
![my-drafts-desktop-wireframe](documentation/images/wireframes/desctop-wireframes/draft-wireframe.png)

#### About page
![about-desktop-wireframe](documentation/images/wireframes/desctop-wireframes/about-wireframe.png)

#### Sign In page
![signin-desktop-wireframe](documentation/images/wireframes/desctop-wireframes/sign-in-wireframe.png)

#### Sign Out page
![signout-desktop-wireframe](documentation/images/wireframes/desctop-wireframes/signout-wireframe.png)

#### Sign Up page
![signout-desktop-wireframe](documentation/images/wireframes/desctop-wireframes/signup-wireframe.png)


#### Mobile Wireframes
Wireframes for Small Screen Sizes

#### Home Page 
![home-page-mobile-wireframe](documentation/images/wireframes/mobile-wireframes/home-mobile-wireframe.png)

#### Posts List page
This page is accessible for just logged-in users
![posts-list-mobile-wireframe](documentation/images/wireframes/mobile-wireframes/posts-list-mobile-wireframe.png)

#### Add Posts page
![add-post-mobile-wireframe](documentation/images/wireframes/mobile-wireframes/add-post-mobile-wireframe.png)

#### Search Posts page
![search-post-mobile-wireframe](documentation/images/wireframes/mobile-wireframes/search-mobile-wireframe.png)

#### My Drafts page
![my-drafts-mobile-wireframe](documentation/images/wireframes/mobile-wireframes/draft-mobile-wireframe.png)

#### About page
![about-mobile-wireframe](documentation/images/wireframes/mobile-wireframes/about-mobile-wireframe.png)

#### Sign In page
![signin-mobile-wireframe](documentation/images/wireframes/mobile-wireframes/signin-mobile-wireframe.png)

#### Sign Out page
![signout-mobile-wireframe](documentation/images/wireframes/mobile-wireframes/signout-mobile-wireframe.png)

#### Sign Up page
![signout-mobile-wireframe](documentation/images/wireframes/mobile-wireframes/signup-mobile-wireframe.png)


### Database Design
![Entity-Relationship-Diagram](documentation/images/database/diagram.png)

- The database ER diagram was designed using [SmartDraw](https://www.smartdraw.com). The main Post model contains all the fields needed for the post to be complete. Additional fields (like category, nutritional value, meals type., etc) can be added to further enhance the website, but the values are not vital for the site to work and can be added later.
- The diagram shows relationaships between the Post model, Comments Model, Like Model and django's allauth User model as follows:
   1. User to Post: One-to-Many (1:M)
       - Each user can create multiple posts.
       - Each post is created by one user.
   2. Post to Comment: One-to-Many (1:M)
       - Each post can have multiple comments.
       - Each comment is associated with one post.
   3. User to Comment: One-to-Many (1:M)
       - Each user can make multiple comments.
       - Each comment is made by one user.

- In summary, User can create multiple posts, and each post is associated with one user. Post can have multiple comments, and each comment is associated with one post. User can make multiple comments, and each comment is made by one user.
- These relationships was implemented using ForeignKey fields in the models. The Post model have a ForeignKey field referencing the User model to represent the creator of the post, and the Comment model have ForeignKey fields referencing both the Post model and the User model to represent the post being commented on and the user making the comment, respectively.

## The Surface Plane

### Design

The website uses clean, simple design with earthy colours and images that showcases the primary goal of the website. The aim here was to keep the site clutter-free so that user can have a smooth straight-forward navigation experience throughout without any chaos and confusion.

#### Typography

- The images in this project are sourced from [Pexels](https://www.pexels.com/) and [Pixabay](https://pixabay.com/). They were specifically selected to correlate with the main purpose of the website and to give user a imagery representation for the post content to increase impact of the design.

## Technologies

### Tools and Technologies
 
- Visual Studio Code - used to develop the website
- [GitHub](https://github.com/) to host the source code. 
- Git to provide the version control to commit and push code to the repository.
- HTML - used to create main static content of the website
- Bootstrap - front end framework used
- CSS- used for website styling
- JavaScript- used to create dynamic content and make page interactive
- Python - used as the main language to code the logic of the page
- Django - framework used
- Heroku - to deploy the app
- ElephantSQL - A free cloud based PostgreSQL database system used for the application database.
- [FontAwesome](https://fontawesome.com/v5/search) v5.15.4 for website icons.
- [Favicon.io](https://favicon.io/) to create the website favicon.
- [Cloudconvert](https://cloudconvert.com/jpg-to-webp) to convert .jpg images into .webp to reduce storage 
    and enhance the website performance.
- [TinyJPG](https://tinyjpg.com/) to optimise images for website.
- Balsamiq to design the wireframes for the website.
- Google Chrome's Lighthouse to test accessibility for desktop and mobile devices.
- [W3C HTML Markup Validator](https://validator.w3.org/) to validate the HTML Code.
- [W3C Jigsaw CSS Validator](https://jigsaw.w3.org/css-validator/) to validate the CSS Code.
- [jshint validator](https://jshint.com/) - used to check java script code for errors.
- [SmartDraw](https://www.smartdraw.com/) used to generate the ER Diagram
- [Am I Responsive](http://techsini.com/) to create the Mockup image in this README.
- Code Institute's Gitpod Template to generate the workspace for the project.
- BrowserStack for cross-browser testing.


### Imports

#### Python Packages
- Summernote - used to provide an editor for user and admin for adding recipes instructions and ingredients.
- TemplateView, CreateView, ListView, DeleteView, UpdateView - used to allow CRUD functionality
- LoginRequiredMixin, UserPassesTestMixin - used to test and secure views from unauthorised access.
- messages - used to add action messages to user on submission
- HttpResponseRedirect, reverse : used to direct user to specific URL
- get_object_or_404: used to get specific object from database or raise 404 exception if not found

#### External Packages

- asgiref - A standard Python library to allow for asynchronous web apps and servers to communicate with  each other.
- cloudinary==1.36.0 - media management cloudinary
- dj3-cloudinary-storage==0.0.6 - cloudinary storage
- dj-database-url==0.5.0 - Django utility allows to utilize DATABASE_URL environment variable to configure 
  Django application
- Django==4.2.9 - Framework used to build the project
- django-allauth==0.57.0 - authentication in django allows users to sign-in / signup / logout
- requests-oauthlib==1.3.1 - installed with the allauth
- psycopg2==2.9.9 - additional dependency needed to support PostgreSQL when deployed on heroku
- django-crispy-forms==2.1 - used to display forms to user
- django-summernote==0.8.20.0 - used to provide editor in forms

Installed as dependencies with other packages:
- gunicorn==20.1.0
- oauthlib==3.2.2
- PyJWT==2.8.0
- python3-openid==3.2.0
- sqlparse==0.4.4
- urllib3==1.26.18

## Testing 

### Responsiveness

- The site is designed to be flexible, fluid and responsive on all screen sizes. Website has been checked for responsiveness through Chrome Development tools. In order to do this, the following steps have been taken:
  1. Open the browser.
  2. Navigate to the Tasty Tales website <https://tasty-tales-4b4d80fd4040.herokuapp.com/>
  3. Right click anywhere on the page and got to "Inspect" to open Development Tools.
  4. Click on drop down menu: "Dimensions: Responsive" and choose "Responsive".
  5. Drag the side of the screen and change screen size, making sure the website looks good from 320px and up. Here, ensure there is consistency in design of the website on every screen size from small(mobile devices) to larger(desktop devices) and no scorll bar is showing for layout of site.

- Expected Result: Each page is responsive and user friendly when viewing the website on small and large screens.The pages have no design or accessibility issue in any of the screen sizes from 320px and up.
- Actual Result: Website is responsive with no scroll bar showing, the content is accessible to user to read and the images are not appearing stretched. Website is user friendly on small to large screen sizes.

- The following devices are used to check responsiveness:
     - Iphone 12 Pro
     - Samsung Galaxy S20 Ultra
     - iPad Mini
     - Surface Pro 7
- The website was also tested further by sharing the live link with friends and family. The site was tested on following devices:
     - Samsung S20 FE 5G
     - Iphone 12 
     - iPad Air
     - Samsung S24 Ultra
     - Microsoft Surface
     - Asus X5 50
     - Lenovo Pad Pro 12.7

- The following browsers have been used to check responsiveness. Testing for different browsers was carried on using [BrowserStack](https://www.browserstack.com/) and manually on some of the browsers.
     - Chrome
     - Safari
     - Microsoft Edge
     - Firefox
     - Internet Explorer

### Accessibility

- Each page is checked with the help of WAVE Accessibility tool (<https://wave.webaim.org/>)
- Each page passes accessibility test with no error for:
  - contrast
  - aria- labels for users who use screen-readers.
  - alternative text as a function for screen readers or in events if the images don't load.
  - structural elements: for users of assistive technology as well as visual and semantic meaning.
  - language of the document for screen readers.
  - an alert coming up 'Reduntant link-Adjacent links go to the same URL', however as it doesn't come up as an error, I have left it in' This is due to page logo and Home page having the same destination link.
  - an alert is coming up 'same alternative text to nearby images' in recipes list view, as the alt is given default in the code, the user uploaded images appear with same alternative text, the solution for this can be adding an image alt field to model, so that the alternative text for image is added by user. I have left it in for later.

![wavw-testing-result](documentation/images/testing/wave-testing.png)

### Lighthouse

### Home Page (Desktop / Mobile)

<details>

  <summary>Home Page - Desktop</summary>
    
![home-page-lighthouse-desktop](documentation/images/testing/light-house-home.png)

  </details>

<details>

  <summary>Home Page - Mobile</summary>
    
![home-page-lighthouse-mobile](documentation/images/testing/home-mobile-lighthouse.png)

  </details>

### Posts Page (Desktop / Mobile)

<details>

  <summary>Posts Page - Desktop</summary>
    
![posts-page-lighthouse-desktop](documentation/images/testing/posts-lighthouse.png)

  </details>

<details>

  <summary>Posts Page - Mobile</summary>
    
![posts-page-lighthouse-mobile](documentation/images/testing/posts-mobile-lighthouse.png)

  </details>

### Add Post Page (Desktop / Mobile)

<details>

  <summary>Add Post Page - Desktop</summary>
    
![add-post-page-lighthouse-desktop](documentation/images/testing/addpost-light-desktop.png)

  </details>

<details>

  <summary>Add Post Page - Mobile</summary>
    
![add-post-page-lighthouse-desktop](documentation/images/testing/addpost-lighthouse-mobile.png)

  </details>

### Search Page (Desktop / Mobile)

<details>

  <summary>Search Page - Desktop</summary>
    
![search-page-lighthouse-desktop](documentation/images/testing/search-desktop-lighthouse.png)

  </details>

<details>

  <summary>Search Page - Mobile</summary>
    
![search-page-lighthouse-desktop](documentation/images/testing/search-mobile-lighthouse.png)

  </details>

### Login Page (Desktop / Mobile)

<details>

  <summary>Login Page - Desktop</summary>
    
![login-page-lighthouse-desktop](documentation/images/testing/signin-desktop-lighthouse.png)

  </details>

<details>

  <summary>Login Page - Mobile</summary>
    
![login-page-lighthouse-desktop](documentation/images/testing/signin-mobile-lighthouse.png)

  </details>
  
### Sign up Page (Desktop / Mobile)

<details>

  <summary>Signup Page - Desktop</summary>
    
![signup-page-lighthouse-desktop](documentation/images/testing/signup-desktop-lighthouse.png)

  </details>

<details>

  <summary>Login Page - Mobile</summary>
    
![signup-page-lighthouse-desktop](documentation/images/testing/signup-mobile-lighthouse.png)

  </details>

### About Page (Desktop / Mobile)

<details>

  <summary>About Page - Desktop</summary>
    
![about-page-lighthouse-desktop](documentation/images/testing/about-desktop-lighthouse.png)

  </details>

<details>

  <summary>About Page - Mobile</summary>
    
![about-page-lighthouse-desktop](documentation/images/testing/about-mobile-lighthouse.png)

  </details>

## Validator Testing

### HTML Validation

All pages have been run through the [W3C VALIDATOR](https://validator.w3.org/).

In order to check HTML code in dynamic website:

- go to the live page
- click right and select 'Inspect' then click right and select 'View page source'
- code will open in new tab - copy the code
- paste the code in the validator as 'direct input'

#### Home Page
![home-page-html-validation](documentation/images/html-validator/home-html-valid.png)

#### Posts Page
![posts-page-html-validation](documentation/images/html-validator/posts-html-valid.png)

#### Drafts Page
![Drafts-page-html-validation](documentation/images/html-validator/draft-html-valid.png)

#### Post Delete Page
![post-delete-page-html-validation](documentation/images/html-validator/post-delete-html-valid.png)

#### Post Detail Page
![post-detail-page-html-validation](documentation/images/html-validator/post-detail-html-valid.png)

#### Search Page
![posts-page-html-validation](documentation/images/html-validator/search-html-valid.png)

#### Add Recipe Page | Update Recipe Page
All errors listed by W3Validator are related to Summernote, and not any code written by me. Errors are the same for both "Add Recipe" page and "Update Recipe" page. Research conducted within the Code Institute community indicates that this is a common occurrence, and therefore it should be noted. However, no action needs to be taken in response.

#### Sign Up Page
 The Sign Up page HTML code is part of the Django authentication form, and I could find no way to change it. 
 The html errors are coming from Django forms interpretation of allauths helper text, and not any code written by me. So, no action is taken in response.
  
### CSS Validation
No errors were found when passing through the official Jigsaw W3 Validator

![css-validation-check](documentation/images/css-validator/css-valid.png)

### JavaScript Validation
No errors were found when passing through the [jshint validator](https://jshint.com/)

![jshint-validation-check](documentation/images/jsvalidator/jshint-validator.png)

### Python Validation
No errors were found when passing each file through [CI Python Linter](https://pep8ci.herokuapp.com/)

![python-validation-check](documentation/images/python-validator/python-validation.png)

Couple of warnings when running settings.py file. Too long lines of code. Modifying the file for resolving the warnings rendered errors during deployment. I have left the mentioned lines in settings.py file unchanged for warnings. All other python files have passed the validation with no errors.

## Manual Testing

### Functional Testing


|  Function   |   Action   |    Expected    |  Actual  |
|-------------|-------------|----------------|----------|
| sign-up   | user clicks- 'sign-up' or 'sign up now', user enters username, password and repeats password,(email optional) user clicks- 'sign-up>>' | user directed to home page, user receives a message of Successfully Signed up as 'USERNAME' at the top of the page |  as expected  |
| sign-in   | user clicks- 'sign-in' from nav bar or from sign-up page if entered it but already holds login details, user enters correct username and password, user clicks- 'sign-in' | user directed to home page, user receives a message of Successfully Signed in as 'Username' at the top of the page | as expected  |
| log-out  | user clicks ' log-out' from nav bar, sign-out page displays to confirm sign-out, user confirms by clicking ' sign-out'  | user directed to home page, user receives a success message of 'You have signed out' at the top of the page | as expected  |
| recipes tab |  user clicks on 'recipes' tab from nav bar | user directed to recipes.html page, a list of 'published' recipes available to view regardless of user auth state. User can see 6 recipe post list per page and pagination navigation available below recipe posts lists if more than 1 pages available | as expected  |
| pagination navigation (from recipes.html, my_drafts.html or recipe_search.html)| user on page 1: can see and clicks on: next. If user is not on page 1: user can see and click on : previous or next page if more than 2 pages available | user gets directed to relevant and correct page depending on which option (next / prev) was clicked | as expected  |
| view recipes (from list view on recipes.html or recipe_search.html)| user hovers over ' view recipe' button, button changes color to dark blue when hovered over, user clicks on the button | recipe_detail.html page rendered for user, user can see correct recipe in detail | as expected  |
| Like function (from recipe_detail page) | 1. logged-in user clicks on hollow heart icon 2. logged-in user clicks on the solid red heart icon 3. unauthorised user clicks on heart icon | 1. icon changes to solid red color and number of likes increases by one. 2.icon changes to hollow and number of likes decreases by One. 3. the hollow heart icon has no effect | as expected  |
| login to leave a comment : sign-in (from recipe_detail page) | user clicks on 'sign-in', user enters correct username and password, then clicks ' sign in' | user redirected back to the same recipe detail page, user can see success message at the top of the screen. upon scrolling down to comments section- user can now see submission form to leave a comment instead of sign-in option | as expected  |
| leave comment form | user enters a comment and clicks submit | users comment now displays in comments section adjacent to the comment form. Comments are shown in reverse chronological order with the oldest comments apperaing first | as expected  |
| My Drafts tab | logged in user clicks on My Drafts tab from nav bar | user directed to my_drafts.html, a list of only users own recipes - 'status - draft' available to view. User can see 6 recipes list per page and pagination navigation available below recipe posts if more than 6 recipes are available. If user didn't create any draft recipe yet a message will be displayed conveying user has no draft recipes yet. | as expected  |
|Add Recipe tab | logged in user clicks on Add Recipe tab from nav bar | user directed to add_recipe.html page where they can see submission form for recipes | as expected  |
| Add Recipe form | user enters all fields marked as required with an '*', the optional image field can either stay empty or be filled in- user clicks 'submit' | user directed back to recipes.html page, a success message displays on the top of the page, user now can see the added recipe post in list view on recipes page. If user submitted the recipe as draft- the recipe displays only on My Drafts page with status of 'Draft', if post was marked as published- it displays as a list view on recipes.html page | as expected  |
| Delete recipe (recipe_detail page ) | user can only see ' delete' button on own published recipes. User clicks on 'delete'. User directed to recipe confirm delete page. 1. user clicks'Yes, Delete Recipe' 2.user clicks 'Cancel' | 1. user is taken back to recipes.html page, success message displayed at the top of the page, recipe deleted 2. user directed back to recipe_details page for the same recipe and recipe remains published. | as expected  |
| Edit recipe (recipe_detail page or my_drafts page) | user can only see 'Edit' button on own recipes. User clicks on 'Edit'. User directed to a edit form on update_recipe.html page . User can change any field and click submit. | user directed back to recipes page, success message displays if recipe is updated succesfully. User can still see the recipe in list view  if published or on the my_drafts page if updated as draft(The update / edit form submission here and in the my_drafts page is same, it will be directed to edit form in both cases on clicking edit/ update button) | as expected |
| Search Recipes tab | user clicks on Search Posts tab from nav bar regardless of auth status | user directed to recipe_search.html page where they can see form to search recipes | as expected  |
| Add Your Recipe link(Search Recipes Page) | user clicks on add your recipe link regardless of auth status | 1. logged-in user directed to add_recipe.html page where they can see form to add page. 2. unauthorised users are directed to sign-in page and can sign up if not. | as expected  |

### Links and Buttons

| Button / Anchor Link / Location | Destination Page | Page Opens In New Tab |
|---------------------------------|------------------|-----------------------|
|TastyTales logo - nav bar	      | index.html	      | no - as expected       |
| Home tab - nav bar	              |  index.html	      |  no - as expected      |
| Recipes tab - nav bar	          |   recipes.html	   | no - as expected      |
|Search Recipes tab - nav bar      |   recipe_search.html | no - as expected    |
| Add Recipe tab - nav bar (for logged-in users only) | add_recipe.html | no - as expected    |
| My Drafts tab - nav bar (for logged-in users only) |  my_drafts.html | no - as expected    | 
|Logout - nav bar(for logged-in users only) | logout.html |	no-as expected  |
| SignUp Now- from index.html(unauthorised users only) | signup.html |	no - as expected |
| Sign Up - nav bar (unauthorised users only) |	signup.html	 |  no - as expected  |
| Sign In - nav bar (unauthorised users only) |	login.html |	no - as expected |
| Sign in - comments section, recipe_detail.html(unauthorised users only) |	login.html| no - as expected |
|Edit - recipe_detail.html(on users own recipes only) | update_recipe.html | no - as expected |
| Delete - recipe_detail.html(on users own recipes only) |	recipe_confirm_delete.html |	no - as expected |
| All recipes - from recipe_search.html (for all users) | recipes.html | no - as expected |
| Add Your Recipe - from recipe_search.html (1. for unauthorised users. 2. for authorised users) | 1.login.html. 2.add_recipe.html | no - as expected |
|"GitHub" Icon - footer | <https://github.com/gayatrig19> | yes - as expected |
|"LinkedIn" Icon - footer | <https://www.linkedin.com/in/gayatri-ghogare-a8099692/> | yes - as expected |

### Negative Testing

Testing is performed on all forms in the website and for user authentication to Create, Update, Delete recipes.

|  Function  |   Action    |    Expected    |  Actual  |
|------------|--------------|---------------|-----------|
|Sign Up   |	user doesn't fill in all required fields (username and password twice), user enters password twice but doesn't match, username enters too common password or less than 8 characters |	user received a prompt with directions, submission unsuccessful user can enter details again | as expected |
|Sign-in |	user doesn't fill in all required fields (username and password). user enters incorrect username or password | user receives prompt why sign-in is unsuccessful and can enter details again |	as expected |
| Add Recipe form | user doesn't fill in all required fields(marked with *) | user receives a prompt to fill in the required field. form doesn't submit. user can enter details again | as expected |
|Edit Recipe |	1.user tries to access URL to edit recipe but not logged in 2. user tries to access the url from different username	| 1.user directed to login page 2. user receives error 403 |	as expected |
| Delete Recipe |	1.user tries to access URL to delete recipe but not logged in 2. user tries to access the url from different username | 1.user directed to login page 2. user receives error 403 | as expected |
| Comment form |	user tries to submit empty comment form |	user receives prompt Please fill in this field, form is not submitted |	as expected |


## Automated Testing

### Unit Testing

Unit testing has many advantages:
 - Firstly it's quicker so I can run many hundreds of tests against my project in a short space of time.
 - Secondly the tests are usually written by programmer as the project is being developed.
 - Thirdly tests can be written for very specific cases.
#### Form testing

##### Instruction
 - create a test_forms.py file in my about app directory and write a class to test my form.

##### CollaborateForm Test (About App)
 - Ensures that all required fields are validated correctly in collaborate form.

![test-fail-in-collaborateform](documentation/images/automated-test/about-test-false.png)

-----

![test-pass-in-collaborateform](documentation/images/automated-test/about-test-true.png)

##### Comment Form Test (blog App)
- Tests if users can submit comments successfully.
- Ensures invalid comments (e.g., empty comments) are rejected.

![test-pass-in-comment-form](documentation/images/automated-test/comment-test-true.png)

-----

![test-fail-in-comment-form](documentation/images/automated-test/comment-test-false.png)

-----

![all-tests-pass-in-comment-form](documentation/images/automated-test/commentform-false-ok.png)

#### Post Form Test (blog App)
- Checks that a blog post form is valid when all fields are correctly filled.
- Ensures missing or incorrect fields trigger validation errors.
 
![test-pass-in-comment-form](documentation/images/automated-test/post-test-true.png)

-----

![test-fail-in-comment-form](documentation/images/automated-test/post-test-false.png)


#### View testing

##### Instruction
 - create a test_views.py file in my about app directory and write a class to test my views.
 - Use of setUp method in my class to setup needed instance variables

##### Blog View Test (Blog App)
    
![blog-page-automate-test](documentation/images/automated-test/blog-view-test-pass.png)


##### About View Test (About App)
    
![about-page-automate-test](documentation/images/automated-test/about-view-test-pass.png)


## Bugs
 - Active attribute didn't work in the navbar because I used wrong way to add active attribute to the nav bar and after talk with tutor I replaced a new way and resolved it.
 - Installing both whitenoise and cloudinary resulted in conflict for serving static files and as a result the deployment failed.
  - Fix: The order of apps in my Installed Apps in settings.py for cloudinary was not correct. The apps are reorder correctly, Whitenoise and related staticfiles folder is removed. Static files are served on Cloudinary.

## Deployment

### Version Control

- The website was developed through Gitpod.

- Code has been pushed to repository on Github with following git commands:

    - git add . - to add files ready to commit
    - git commit -m "message" - to commit the code to local repository ready to be pushed
    - git push - final command used to push committed code to remote repo on Github


### Deployment In Heroku

- The project has been deployed on Heroku as follows:
     - Use: pip freeze > requirements.txt to add external libraries to deployed app.
     - Create Heroku account
     - In the top right, click 'New'
     - Click 'Create new app'
     - Give your app a name and select your region from drop down
     - Click 'Create new app'
     - Go to 'settings' tab, it's important you do it before deployment
     - Scroll down to 'config vars' section and key:
          - PORT and value: 8000
          - CLOUDINARY_URL: 'API key to your cloudinary account'
          - DATABASE_URL : 'URL from your database account'
          - SECRET_KEY: 'Generate your own secret key'
     - Scroll down to 'Buildpacks' section
     - Click 'Add buildpack'
     - Add Python as first dependency and select 'Save changes'
     - Add node.js as a second dependency and save again (This is settings section done)
     - Select 'Deploy' tab at the top
     - Select 'Github' from 'Deployment method'
     - type the name of how you called project in Github and click 'search'
     - Scroll down and select manual deployment method
     - You can also use Auto deployment method to allow the project to update every time you push the code.
     - You can now click to view the app ready and running
- For this project I used Manual deployment method to deploy the current state of the branch, every time I pushed the code from Gitpod.


### Cloning the Repository

1. On Github navigate to the repository
2. Click "Code" drop down menu - a green button shown right above the file list.
3. Copy the URL of the repository using "HTTPS", "SSH" or "Github CLI".
4. Open Git Bash.
5. Change the current working directory to the location where you want the cloned directory.
6. Type "git clone", and then paste the URL copied earlier.
7. Press enter to create local clone. A clone of the repository will now be created.

For more details on how to clone the repository in order to create a copy for own use refer to the site: <https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository>


### Forking 

1. On Github navigate to the repository.
2. Click "Fork" located towards top right corner on GitHub page.
3. Select "owner" for the forked repository from the dropdown menu under "owner".
4. It will create forked repo under the same name as original by default. But you can type a name in "Repository name" or add a description in "Description" box.
5. Click on "Create fork". A forked repo is created.

- Forking allows you to make any changes without affecting original project. You can send the the suggestions by submitting a pull request. Then the Project Owner can review the pull request before accepting the suggestions and merging them.
- When you have fork to a repository, you don't have access to files locally on your device, for getting 
  access you will need to clone the forked repository.
- For more details on how to fork the repo, in order to for example suggest any changes to the project you can visit:<https://docs.github.com/en/get-started/quickstart/fork-a-repo>


## Credits

- I learned many things from Gayatrig project and it helped me alot. [Gayatrig-tastytales-website](https://tasty-tales-4b4d80fd4040.herokuapp.com/)
- All images used on the website are sourced from [Pexels](https://www.pexels.com/), [Pixabay](https://pixabay.com/) and [Unsplash.](https://unsplash.com/)
- Code Institute's "I Think Therefore I Blog" walkthrough project was referred throughout during development.
- [Django Documentation](https://docs.djangoproject.com/en/4.2/) helped me in understanding the class based views and search functionality.
- Ability to create and update recipe post while getting a success message displayed is achieved by following instructions in Stack Overflow article. [Create/Update Recipe](https://stackoverflow.com/questions/67366138/django-display-message-after-creating-a-post)
- [Recipe Tutorial](https://www.youtube.com/watch?v=ZCPhzoK_bg4&list=PLXuTq6OsqZjbCSfiLNb2f1FOs8viArjWy&index=3) helped me to get started with the files setup and base structure.
- The code for deleting recipe is referred from this [Recipe Tutorial.](https://www.youtube.com/watch?v=nFa3lC105dM&list=PLXuTq6OsqZjbCSfiLNb2f1FOs8viArjWy&index=13)
- [Readme](https://github.com/Gareth-McGirr/Portfolio-Project-4-SizzleAndSteak/tree/main?tab=readme-ov-file#heroku-deployment) used for basic readme structure.
- [Blog Tutorial](https://www.youtube.com/watch?v=B40bteAMM_M&list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi) helped me in creating my models and understanding the CRUD functionality.
- The PositiveInteger validation for cooking time, prep time and servings was referred from this [article.](https://stackoverflow.com/questions/2248617/0-value-in-django-positiveintegerfield)
- The search functionality in django was studied from this [tutorial](https://learndjango.com/tutorials/django-search-tutorial) and modified according to the project requirements.

## Acknowledgements

- I would like to express my gratitude to my mentor, Can Sücüllü, for his unwavering guidance, moral support, encouragement, and invaluable suggestions throughout the project. The project review sessions with my mentor, along with his solutions to my questions and the study materials he provided, were instrumental in the success of this project.
- I am grateful to the Code Institute's Tutor support for solving all my doubts.









































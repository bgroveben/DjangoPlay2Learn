# DjangoPlay2Learn
## Adding the Backend

In this project, you will be creating the backend for the Play2Learn website.
The website should allow users to log in to the site, play games, track their progress, see leaderboards, manage their account, and leave reviews.
Administrators will be able to run reports and manage users.
Any visitor to the site should also be able to fill out a contact us form.
You should be using Python and Django to add the backend.
You can use the JavaScript games you've created in previous projects.


Run Vue app on home page with links to both games using Vue routes and components. Pass scores and any other data to Django.

Vue handles routing and components.
Axios lets the frontend and backend talk to each other with http.
Django handles the REST framework as well as models for the Postgres DB.

– Django exports REST Apis using Django Rest Framework & interacts with Database using Django Model.
– Vue Client sends HTTP Requests and retrieve HTTP Responses using axios, shows data on the components. We also use Vue Router for navigating to pages.

serializers.py
axios-api.js
pip install django-cors-headers

Configure Vue to not interfere with the Django template syntax (both use {{}} as delimiters). Try [[]] instead.
https://www.reddit.com/r/vuejs/comments/b93cxb/django_template_tags_in_vue_components/ -- render Vue components in Django template.
Create pages app for home, about-us, maybe the contact page? Or use the ones in the Vue app?
Static files for favicon, logo, and css stylesheet?
Email confirmation of registration?

Use Postgres database on the assignment page to set your models.

Graded:
    Integrate Vue games -- Lessons 3, 6
    Login and Registration -- Lessons 10, 11
    Game Tracking and Leaderboards -- Lesson 9
    Reviews -- Lesson 13.JokeVote Model
    Contact Us Page -- Lesson 8
    Admin Site -- Lessons 5,17


https://www.webucator.com/article/connecting-django-and-vue/
-- Ajax and Vue
https://codewithstein.com/combining-django-and-vuejs-everything-you-need-to-know/

https://www.bezkoder.com/django-vue-js-rest-framework/
https://www.bezkoder.com/django-postgresql-crud-rest-framework/
https://www.bezkoder.com/vue-3-crud/

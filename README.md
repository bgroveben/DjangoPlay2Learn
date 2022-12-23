# DjangoPlay2Learn
## Adding the Backend

In this project, you will be creating the backend for the Play2Learn website.
The website should allow users to log in to the site, play games, track their progress, see leaderboards, manage their account, and leave reviews.
Administrators will be able to run reports and manage users.
Any visitor to the site should also be able to fill out a contact us form.
You should be using Python and Django to add the backend.
You can use the JavaScript games you've created in previous projects.


User cannot log in or register from site, only admin works for login
Logged in users can update their account information
SuccessMessageMixin works in admin but not on site
https://django-allauth.readthedocs.io/en/latest/views.html

-- Login, Signup, and Logout views

-- https://ordinarycoders.com/blog/article/django-user-register-login-logout
    -- add register path to app URLs so we can refer to it in views, ex
        -- path("register", views.register_request, name="register")
    -- create register_request(request) function to register user

-- https://learndjango.com/tutorials/django-signup-tutorial


Fix your routes and urls so that you redirect users to the correct view after they make a POST request like a login or password change
http://127.0.0.1:8000/account/password/change/
Reverse for 'my-account' not found. 'my-account' is not a valid view function or pattern name.

http://127.0.0.1:8000/account/login/
AttributeError at /account/login/
'NoneType' object has no attribute 'method'

http://127.0.0.1:8000/accounts/my-account/
'account' is not a registered namespace
-- only throws error when user isn't logged in

http://127.0.0.1:8000/accounts/confirm-email/Mg:1p8UeA:ESTNjv66hJbFFZCFp9izCgdDA0le7YhAfNXALv-gljc/
NoReverseMatch at /accounts/confirm-email/Mg:1p8UeA:ESTNjv66hJbFFZCFp9izCgdDA0le7YhAfNXALv-gljc/
'account' is not a registered namespace

http://127.0.0.1:8000/users/my-account/
NoReverseMatch at /users/my-account/
'account' is not a registered namespace


Game tracking and Leaderboards--
--common/utils/queries.py -> sql queries to display top scores?

Graded:
    * Integrate Vue games -- Lessons 3, 6
    Login and Registration -- Lessons 10, 11
    * Game Tracking and Leaderboards -- Lesson 2.17 ListView, Lesson 9
    Reviews -- Lesson 9.5 JokeForm(ModelForm), Lesson 13.JokeVote Model
    Contact Us Page -- Lesson 8
    * Admin Site -- Lessons 5,17

    -- django admin ->  username:superuser  password:password

Reviews and comments
-- https://www.django-rest-framework.org/api-guide/serializers/
-- https://www.ericsdevblog.com/posts/create-a-modern-application-with-django-and-vue-3/

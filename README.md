# DjangoPlay2Learn
## Adding the Backend

In this project, you will be creating the backend for the Play2Learn website.
The website should allow users to log in to the site, play games, track their progress, see leaderboards, manage their account, and leave reviews.
Administrators will be able to run reports and manage users.
Any visitor to the site should also be able to fill out a contact us form.
You should be using Python and Django to add the backend.
You can use the JavaScript games you've created in previous projects.


Game tracking:
https://codefellows.github.io/sea-python-401d5/lectures/django_cbv2.html#the-get-object-method


Login and Registration: 25%
DONE (10%) Users can register.
DONE (5%) Registered users can log in and log out.
DONE (10%) Logged in users can edit their information in a My Account page.


Game Tracking and Leaderboards: 30%
* AnonymousUser(s) have scores added to the leaderboard
DONE (5%) Game tracking page exists for both games.
DONE (5%) Leaderboards exist for both games.
DONE (10%) Game tracking shows just the user’s scores.
DONE (10%) Leaderboards shows all the scores.

Reviews: 10%
-- Have username recorded automagically when form is submitted
DONE (5%) Logged-in users can successfully leave reviews.
DONE (5%) User reviews rotate in the slideshow on the homepage.

Contact Us: 10%
DONE (10%) The contact us form sends an email to the admin email.

DONE Admin Site: 25%
DONE (5%) Admin users can access the admin site.
DONE (10%) Admin users can view user data.
DONE (10%) Admin users can update and delete user data.


{% startbugs %}
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

BUGS BELOW

User can choose any username on Review form.

User records score when the game ends by clicking play again or change settings. Add button to record score and redirect to the leaderboard?

SuccessMessageMixin works in admin but not on site
https://django-allauth.readthedocs.io/en/latest/views.html

-- Login, Signup, and Logout views
    -- non-authenticated users see an error when they try to view the my accounts page.
    Make sure that they can't get to /accounts/my-account/
    Redirect urls?
    http://127.0.0.1:8000/users/my_account/
    -> NoReverseMatch at /users/my_account/
    'account' is not a registered namespace
    -- logged-in users who log in again get a 403
    Forbidden (403)
    CSRF verification failed. Request aborted.
    Help
    Reason given for failure:
    CSRF token from POST incorrect.
    http://127.0.0.1:8000/accounts/login/

END BUGS
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
{% endbugs %}

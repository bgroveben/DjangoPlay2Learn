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

??? Put the games on the home page with the carousel?
??? Organize reviews by created date?
??? Make font sizes on scores pages smaller?
!!! CharField requires a length restriction, TextField doesn't.
!!! Make sure all of your POST requests redirect.
!!! Setup, Exercise, Assert is the typical structure for a unit test.


NEXT: TESTS

$=> coverage run --omit='*/venv/*' manage.py test
$=> coverage report
$=> coverage html


functional - started
common?
users - started
contact - started
games - started
review - started

https://www.obeythetestinggoat.com/book/chapter_post_and_database.html#_saving_the_post_to_the_database

Django Testing Tutorial
https://www.youtube.com/playlist?list=PLbpAWbHbi5rMF2j5n6imm0enrSD9eQUaM

* Use unittest
* Use Django’s test client to establish that the correct template is being rendered and that the template is passed the correct context data.
* Use RequestFactory to test view functions directly, bypassing the routing and middleware layers.
* Use in-browser frameworks like Selenium to test rendered HTML and the behavior of web pages, namely JavaScript functionality. Django also provides special support for those frameworks; see the section on LiveServerTestCase for more details.

It’s a good idea to run your tests with Python warnings enabled: python -Wa manage.py test. The -Wa flag tells Python to display deprecation warnings.
!!! The test client does not require the web server to be running.

The test client is not capable of retrieving web pages that are not powered by your Django project. Vue games should have separate tests, and only the part where Django talks to Vue needs testing.





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
!!!!!! Don't forget to remove unused code!!!!!!
BUGS BELOW

common app has to be tested with unittest because it's not a django app
-- [project_root]=> python3 manage.py test common
--(.venv) ➜  DjangoPlay2Learn git:(main) => python3 manage.py test common


User records score when the game ends by clicking play again or change settings. Add button to record score and redirect to the leaderboard?
-- record score, then redirect to either the leaderboard, start, or menu

SuccessMessageMixin works in admin but not on site
https://django-allauth.readthedocs.io/en/latest/views.html

-- Login, Signup, and Logout views
    -- non-authenticated users see an error when they try to view the my accounts page.
    ??? Try if user.is_authenticated else clause
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

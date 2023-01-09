# DjangoPlay2Learn
## Adding the Backend

In this project, you will be creating the backend for the Play2Learn website.
The website should allow users to log in to the site, play games, track their progress, see leaderboards, manage their account, and leave reviews.
Administrators will be able to run reports and manage users.
Any visitor to the site should also be able to fill out a contact us form.
You should be using Python and Django to add the backend.
You can use the JavaScript games you've created in previous projects.

NEXT:
Login and Registration: 25%
DONE (10%) Users can register.
DONE (5%) Registered users can log in and log out.
NEXT : (10%) Logged in users can edit their information in a My Account page.
??? !!! Can users change their password, or does the POST request fail?
!!! Click on email confirmation link => NoReverseMatch:
--- 'account' is not a registered namespace

Game Tracking and Leaderboards: 30%
!!! users can record each score more than once; needs redirect to leaderboard
??? should anonymous users have scores added to the leaderboard?
(5%) Game tracking page exists for both games.
DONE (5%) Leaderboards exist for both games.
(10%) Game tracking shows just the user’s scores.
DONE (10%) Leaderboards shows all the scores.

Reviews: 10%
(5%) Logged-in users can successfully leave reviews.
--- ??? Only admin can leave reviews
(5%) User reviews rotate in the slideshow on the homepage.

Contact Us: 10%
DONE (10%) The contact us form sends an email to the admin email.
https://www.twilio.com/blog/build-contact-form-python-django-twilio-sendgrid
https://ordinarycoders.com/blog/article/build-a-django-contact-form-with-email-backend
-- BadHeaderError to prevent attackers from adding headers
https://www.youtube.com/watch?v=1ihn3iRXtsY

DONE Admin Site: 25%
DONE (5%) Admin users can access the admin site.
DONE (10%) Admin users can view user data.
DONE (10%) Admin users can update and delete user data.


Check the database tables shown in the assignment for help with models.
{% startbugs %}
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
BUGS BELOW
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


REVIEWS -- SUBMIT FORM AND RECORD COMMENT AND VOTES
Lesson 2:22 Creating and Updating Jokes
/jokes/ ~= /users/
set up slugs
check models -> Joke Model = Review Model -> question=game, answer=comment
                JokeListView = ReviewListView
                JokeVoteAdmin -> 'joke' = 'review'
check urls
-- http://127.0.0.1:8000/users/reviewspage/
    405 error on review submission, but link to reviewspage works
    https://stackoverflow.com/questions/68270841/405-error-method-is-not-allowed-python-django
check form
check view
vote function to register reviews

Game tracking and Leaderboards--
--common/utils/queries.py -> sql queries to display top scores?
-- async recordScore() in AH and MF components for data passed to games view and game-scores template

-- form, template(Bootstrap slideshow on homepage), model, view, admin, urls
https://github.com/bunnythecompiler/movie_review/tree/master/movie
https://blog.devgenius.io/lets-build-a-movie-review-django-app-47658f8e3751
-- leave a comment and star rating for MF or AH
-- review model has a many-to-one relationship with user
https://docs.djangoproject.com/en/4.1/topics/db/examples/many_to_one/

Reviews and comments
-- https://michaelstromer.nyc/books/intro-to-django/django-reviews
-- https://www.django-rest-framework.org/api-guide/serializers/
-- https://www.ericsdevblog.com/posts/create-a-modern-application-with-django-and-vue-3/

Graded:
    * Integrate Vue games -- Lessons 3, 6
    * Login and Registration -- Lessons 10, 11
    * Game Tracking and Leaderboards -- Lesson 2.17 ListView, Lesson 8,9
    * Reviews -- Lesson 9.5 JokeForm(ModelForm), Lesson 13.JokeVote Model
    * Contact Us Page -- Lesson 8,9
    * Admin Site -- Lessons 5,17

    -- django admin ->  username:superuser  password:password


Reviews and comments
-- https://www.django-rest-framework.org/api-guide/serializers/
-- https://www.ericsdevblog.com/posts/create-a-modern-application-with-django-and-vue-3/

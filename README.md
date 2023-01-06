# DjangoPlay2Learn
## Adding the Backend

In this project, you will be creating the backend for the Play2Learn website.
The website should allow users to log in to the site, play games, track their progress, see leaderboards, manage their account, and leave reviews.
Administrators will be able to run reports and manage users.
Any visitor to the site should also be able to fill out a contact us form.
You should be using Python and Django to add the backend.
You can use the JavaScript games you've created in previous projects.

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
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
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

Check the database tables shown in the assignment for help with models.


REVIEWS -- SUBMIT FORM AND RECORD COMMENT AND VOTES
/jokes/ ~= /users/
set up slugs
check models -> Jokes Model = Review Model -> question=game, answer=comment
                JokeListView = ReviewListView
check urls
-- http://127.0.0.1:8000/users/reviewspage/
    405 error on review submission, but link to reviewspage works
    https://stackoverflow.com/questions/68270841/405-error-method-is-not-allowed-python-django
check form
check view
vote function to register reviews




-- form, template(Bootstrap slideshow on homepage), model, view, admin, urls
https://github.com/bunnythecompiler/movie_review/tree/master/movie
https://blog.devgenius.io/lets-build-a-movie-review-django-app-47658f8e3751
-- leave a comment and star rating for MF or AH
-- review model has a many-to-one relationship with user
https://docs.djangoproject.com/en/4.1/topics/db/examples/many_to_one/
https://michaelstromer.nyc/books/intro-to-django/django-reviews



Game tracking and Leaderboards--
--common/utils/queries.py -> sql queries to display top scores?
-- async recordScore() in AH and MF components for data passed to games view and game-scores template

Graded:
    * Integrate Vue games -- Lessons 3, 6
    * Login and Registration -- Lessons 10, 11
    * Game Tracking and Leaderboards -- Lesson 2.17 ListView, Lesson 9
    Reviews -- Lesson 9.5 JokeForm(ModelForm), Lesson 13.JokeVote Model
    Contact Us Page -- Lesson 8
    * Admin Site -- Lessons 5,17

    -- django admin ->  username:superuser  password:password


Reviews and comments
-- https://www.django-rest-framework.org/api-guide/serializers/
-- https://www.ericsdevblog.com/posts/create-a-modern-application-with-django-and-vue-3/

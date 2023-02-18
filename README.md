# DjangoPlay2Learn
## Adding the Backend

In this project, you will be creating the backend for the Play2Learn website.
The website should allow users to log in to the site, play games, track their progress, see leaderboards, manage their account, and leave reviews.
Administrators will be able to run reports and manage users.
Any visitor to the site should also be able to fill out a contact us form.
You should be using Python and Django to add the backend.
You can use the JavaScript games you've created in previous projects.

This project was built using Python, Django, Vue, Node, and Bootstrap as well as HTML, CSS, and Javascript. We were taught Postgres, but I used a SQLite database instead because it's easier and the assignment didn't forbid it.

## Instructions

1. Open a prompt/shell/terminal/etc in the root project directory.
2. Activate your virtualenv
3. => python3 manage.py runserver 
4. Open a new terminal in vue-games app directory.
5. => npm run serve

You should have the Django application running at
    http://127.0.0.1:8000/#/
and the Vue application running at
    http://127.0.0.1:8080/#/


THEN: Comment and document your code

TESTS:
$=> coverage run --omit='*/venv/*' manage.py test
$=> coverage report  # PRINT TO TERMINAL
$=> coverage html    # PRINT TO FILE
$=> open -a "Google Chrome" htmlcov/index.html


!!!!!!!! GRADED !!!!!!!!!!

Login and Registration: 25%
DONE (10%) Users can register.
DONE (5%) Registered users can log in and log out.
DONE (10%) Logged in users can edit their information in a My Account page.
-- A confirmation email is sent on registration, but the user is logged in immediately anyway. I like it this way.

Game Tracking and Leaderboards: 30%
* AnonymousUser(s) have scores added to the leaderboard
DONE (5%) Game tracking page exists for both games.
DONE (5%) Leaderboards exist for both games.
DONE (10%) Game tracking shows just the user’s scores.
DONE (10%) Leaderboards shows all the scores.

Reviews: 10%
DONE (5%) Logged-in users can successfully leave reviews.
DONE (5%) User reviews rotate in the slideshow on the homepage.
-- The assignment doesn't specify form validation. Let the browser do it.

Contact Us: 10%
DONE (10%) The contact us form sends an email to the admin email.

DONE Admin Site: 25%
DONE (5%) Admin users can access the admin site.
DONE (10%) Admin users can view user data.
DONE (10%) Admin users can update and delete user data.

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# DjangoPlay2Learn
## Adding the Backend

In this project, you will be creating the backend for the Play2Learn website.
The website should allow users to log in to the site, play games, track their progress, see leaderboards, manage their account, and leave reviews.
Administrators will be able to run reports and manage users.
Any visitor to the site should also be able to fill out a contact us form.
You should be using Python and Django to add the backend.
You can use the JavaScript games you've created in previous projects.


NEXT:
-- UPDATE view with new ReviewForm instance
-- Change votes widget on ReviewForm into something not hideous
-- Validate html and css
-- time is not local
    - a score recorded after 4pm locally is posted with tomorrow's date.
    -Should I care?
??? Semantic html for the folks with special needs ???

THEN: Comment and document your code

$=> coverage run --omit='*/venv/*' manage.py test
$=> coverage report
$=> coverage html
$=> open -a "Google Chrome" htmlcov/index.html


!!!!!!!! GRADED !!!!!!!!!!

Login and Registration: 25%
DONE (10%) Users can register.
DONE (5%) Registered users can log in and log out.
DONE (10%) Logged in users can edit their information in a My Account page.
-- confirmation email is sent on registration, but user is logged in immediately. I like it this way.

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

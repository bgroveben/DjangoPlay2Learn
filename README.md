# DjangoPlay2Learn
## Play2Learn Complete Website Project

**This project was built using Python, Django, Vue, Node, and Bootstrap as well as HTML, CSS, and Javascript. We were taught Postgres, but I used a SQLite database instead because it's easier and the assignment didn't forbid it.**

## Assignment:

>In this project, you will be creating the backend for the Play2Learn website.
 The website should allow users to log in to the site, play games, track their progress, see leaderboards, manage their account, and leave reviews.
Administrators will be able to run reports and manage users.
Any visitor to the site should also be able to fill out a contact us form.
You should be using Python and Django to add the backend.
You can use the JavaScript games you've created in previous projects.

## Instructions

1. Open a prompt, shell, terminal, or whatever you use in the root project directory.
2. Activate your virtualenv
3. `$=> python3 manage.py runserver`
4. Open a new terminal in vue-games app directory.
5. `$=> npm install`
6. `$=> npm run serve	`

You should have the Django application running at:
http://127.0.0.1:8000/#/
and the Vue application running at:
http://127.0.0.1:8080/#/

**TESTS:**
`$=> python3 manage.py test`
*To view test coverage:*
`$=> coverage run --omit='*/venv/*' manage.py test`
`$=> coverage report` # PRINT TO TERMINAL
`$=> coverage html ` # PRINT TO FILE
`$=> open -a "browser name here"
htmlcov/index.html`

## ==GRADING==

- If you want to see how the scores are displayed, you're just gonna have to play the games and add them yourself. 
- No reviews means no slideshow. Same idea as the scores thing.

**LOGIN AND REGISTRATION: 25%**
(10%) Users can register.
(5%) Registered users can log in and log out.
 (10%) Logged in users can edit their information in a My Account page.
 
- A confirmation email is sent on registration, but the user is logged in immediately anyway. I like it this way.  
- Any confirmation or password reset emails go through Sendgrid and will probably end up in your spam filter because they are from example.com.

**GAME TRACKING AND LEADERBOARDS: 30%**
(5%) Game tracking page exists for both games.
(5%) Leaderboards exist for both games.
(10%) Game tracking shows just the user’s scores.
(10%) Leaderboards shows all the scores.

- AnonymousUser(s) have their scores added to the leaderboard.
- If you want to cheat at the anagrams game, open the dev tools console.[^1]
- If you want to cheat at the math game, use a calculator.
- Scores aren't recorded using local time, so if the date is wrong, that's life.

**REVIEWS: 10%**
(5%) Logged-in users can successfully leave reviews.
(5%) User reviews rotate in the slideshow on the homepage.

**CONTACT US: 10%**
(10%) The contact us form sends an email to the admin email.

- The assignment doesn't specify form validation, so I chose client-side and let the browser do the work.
- Not using server-side validation in the real world is a bad idea, but I was more worried about improving my poor test coverage as well as my poor UX/UI skills.

**ADMIN SITE: 25%**
(5%) Admin users can access the admin site.
(10%) Admin users can view user data.
(10%) Admin users can update and delete user data.

[^1]: `AnagramHunt.vue` line 141
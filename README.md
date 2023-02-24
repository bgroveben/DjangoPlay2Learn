# DjangoPlay2Learn

## Play2Learn Complete Website Project

**This project was built using HTML, CSS, Javascript, Python, Django, Vue, and Bootstrap. I was taught Postgres, but I used a SQLite database instead because it was easier and the assignment didn't forbid it.**

For more information about Django and setting up a development environment to run this app, see the [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django).

## The Assignment:

In this project, I'm creating the backend for the Play2Learn website. The website allows users to log in to the site, play games, track their progress, see leaderboards, manage their account, and leave reviews. Administrators can run reports and manage users. Any visitor to the site can fill out a contact us form. I'm using Python and Django to add the backend. I'm also using the JS games I built for the Play2Learn Website 2 Project.

## Instructions

You'll need a [SendGrid](https://sendgrid.com/) account. Email settings in `settings.py` begin on line 122 with your SENDGRID_API_KEY.

I put my SENDGRID_API_KEY in a `local_settings.py` file that was kept out of version control.

I also left a populated database that you can use, but I'm not giving you the admin password :)

**Note to instructor(s):**

I set up my SendGrid account just like I was taught in Lesson 7 of the Django course.
Hopefully that makes it easier to get this app up and running so you can grade the thing.

1. Unzip the file
2. Open a prompt, shell, terminal, or whatever you use in the root project directory.
3. `$=> python3 -m venv .venv`
4. Activate your virtualenv
5. `$=> pip install -r requirements.txt`
6. `$=> python3 manage.py runserver`
7. Open a new terminal in vue-games app directory.
8. `$=> npm install`
9. `$=> npm run serve	`

You should have the Django application running at:

http://127.0.0.1:8000/#/

and the Vue application running at:

http://127.0.0.1:8080/#/

If you want to run this app on your localhost, update `settings.py` accordingly.

**TESTS:**

`$=> python3 manage.py test`

**To view test coverage:**

`$=> coverage run --omit='*/venv/*' manage.py test`

`$=> coverage report` # PRINT TO TERMINAL

`$=> coverage html ` # PRINT TO FILE

`$=> open -a "browser name here" htmlcov/index.html`

## GRADING

- If you want to see how the scores are displayed, you're just gonna have to play the games and add them yourself. 
- No reviews means no slideshow. Same idea as the scores thing.

**LOGIN AND REGISTRATION: 25%**

(10%) Users can register.

(5%) Registered users can log in and log out.

(10%) Logged in users can edit their information in a My Account page.
 
- A confirmation email is sent on registration, but the user is logged in immediately anyway. I really need to work on the patience thing.
- Any confirmation or password reset emails go through Sendgrid and will probably end up in your spam filter because they are from example.com.

**GAME TRACKING AND LEADERBOARDS: 30%**

(5%) Game tracking page exists for both games.

(5%) Leaderboards exist for both games.

(10%) Game tracking shows just the user's scores.

(10%) Leaderboards show all the scores.

- AnonymousUser(s) have their scores added to the leaderboard.
- If you want to cheat at the anagrams game, open the dev tools console.[^1]
- If you want to cheat at the math game, use a calculator.
- Scores are recorded and displayed in UTC. If you want to change the time zone, you can choose from a list of options found [here](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).

**REVIEWS: 10%**

(5%) Logged-in users can successfully leave reviews.

(5%) User reviews rotate in the slideshow on the homepage.

- The slideshow displays all reviews. If there are none, add them. 

**CONTACT US: 10%**

(10%) The contact us form sends an email to the admin email.

- The assignment doesn't specify form validation, so I chose client-side and let the browser do the work.
- Not using server-side validation in the real world is a bad idea, but I was more worried about improving my poor test coverage as well as my poor UX/UI skills.

**ADMIN SITE: 25%**

(5%) Admin users can access the admin site.

(10%) Admin users can view user data.

(10%) Admin users can update and delete user data.

- I really like Django's admin. This was the most straightforward (and least worrisome) part of the assignment for me.

[^1]: `vue-games/src/components/AnagramHunt.vue` lines 140, 154

# DjangoPlay2Learn
## Adding the Backend

In this project, you will be creating the backend for the Play2Learn website.
The website should allow users to log in to the site, play games, track their progress, see leaderboards, manage their account, and leave reviews.
Administrators will be able to run reports and manage users.
Any visitor to the site should also be able to fill out a contact us form.
You should be using Python and Django to add the backend.
You can use the JavaScript games you've created in previous projects.

Should I leave vue-games in the djangovue_project directory?
Or should I have a fronted-vue directory next to a backend-django directory in the root directory?

Use computed properties? -- Vue Lesson 2.10




!!!!!!
psycopg2.errors.UndefinedTable: relation "games_gamescore" does not exist
LINE 1: INSERT INTO "games_gamescore" ("user_name", "game", "score",...
!!!!!!
-- Try updating the model without username and migrating the db
-- or should i just leave username in and get the model to work?
-- change user-name and user_name to just username

https://v2.vuejs.org/v2/cookbook/using-axios-to-consume-apis.html?redirect=true
https://www.digitalocean.com/community/tutorials/vuejs-rest-api-axios
https://www.educative.io/answers/how-to-make-an-axios-post-request




Run Vue app on home page with links to both games using Vue routes and components. Pass scores and any other data to Django.
-- data: operations, score, gameLength, timeLeft, need to add userName
-- methods: recordScore()
https://vsupalov.com/vue-js-in-django-template/
-- don't forget about context
    -> context["items_json"] = json.dumps(items)
Use VueAxios and axios in MathFacts.vue and AnagramHunt.vue component script tags? https://axios-http.com/docs/example

Reviews and comments -- https://www.django-rest-framework.org/api-guide/serializers/

Configure Vue to not interfere with the Django template syntax (both use {{}} as delimiters). Try [[]] instead.
Configue Django urls to find Vue Components.
Use current homepage and url for games page, make a different Home page.
Static files for favicon, logo, and css stylesheet?
Email confirmation of registration?

Use Postgres database on the assignment page to set your models.

Graded:
    Integrate Vue games -- Lessons 3, 6
    Login and Registration -- Lessons 10, 11
    Game Tracking and Leaderboards -- Lesson 2.17 ListView, Lesson 9
    Reviews -- Lesson 9.5 JokeForm(ModelForm), Lesson 13.JokeVote Model
    Contact Us Page -- Lesson 8
    Admin Site -- Lessons 5,17


https://www.webucator.com/article/connecting-django-and-vue/
-- Ajax and Vue
https://codewithstein.com/combining-django-and-vuejs-everything-you-need-to-know/
https://www.ericsdevblog.com/posts/create-a-modern-application-with-django-and-vue-3/ user comments and reviews
Review model, each review belongs to one user

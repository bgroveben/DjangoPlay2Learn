# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `#managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser

from django.core.exceptions import ValidationError
from django.core.files.images import get_image_dimensions

#from common.utils.text import unique_slug

# It’s perfectly OK to relate a model to one from another app. To do this,
# import the related model at the top of the file where your model is
# defined. Then, refer to the other model class wherever needed.

# from games.models import GameScores


def validate_avatar(value):
    w, h = get_image_dimensions(value)
    if w > 200 or h > 200:
        raise ValidationError('Avatar must be no bigger than 200x200 pixels.')


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    # https://stackoverflow.com/questions/35803443
    # /what-parameters-does-djangos-models-do-nothing-expect
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('CustomUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        #managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class GamesGamescores(models.Model):

    id = models.BigAutoField(primary_key=True)
    username = models.TextField()
    game = models.TextField()
    score = models.IntegerField()
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'games_gamescores'


#class CustomUser(models.Model):
class CustomUser(AbstractUser):
    # https://docs.djangoproject.com/en/4.1/topics/db/examples/many_to_one/
    # see Reviews below
    # review = models.TextField(max_length=200) ??
    # reviews = models.ManyToManyField('Review', blank=True) ??
    # -- you just have to relate users and reviews, not games
    # -- or should I do it anyway?

    # CustomUser.objects.values()
    dob = models.DateField(
        verbose_name="Date of Birth", null=True, blank=True
    )
    avatar = models.ImageField(upload_to='avatars/', blank=True,
        help_text='Image must be 200px by 200px.',
        validators=[validate_avatar]
    )

    def get_absolute_url(self):
        return reverse('my_account')

    def __str__(self): # Do I need this?
        return f'{self.first_name} {self.last_name} ({self.username})'

    class Meta:
        #managed = False
        db_table = 'users_customuser'


class CustomUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    #customuser = models.ForeignKey(UsersCustomuser, models.DO_NOTHING)
    customuser = models.ForeignKey(CustomUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        #managed = False
        #db_table = 'users_customuser_groups'
        unique_together = (('customuser', 'group'),)


class CustomUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    #customuser = models.ForeignKey(UsersCustomuser, models.DO_NOTHING)
    customuser = models.ForeignKey(CustomUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        #managed = False
        #db_table = 'users_customuser_user_permissions'
        unique_together = (('customuser', 'permission'),)


#@classmethod ?
#@login_required ?
# class ReviewUpdate(Review) ?
# class ReviewDelete(Review) ?
class Review(models.Model):
    """
    review = Review(
        vote=1,
        comment="comment",
        game="game",
        customuser=CustomUser.objects.first(),
        created=datetime.now(),
        updated=datetime.now())
    """
    # https://docs.djangoproject.com/en/4.1/topics/db/examples/many_to_one/
    vote = models.SmallIntegerField()
    comment = models.TextField(max_length=200)
    game = models.CharField(max_length=20)
    customuser = models.ForeignKey(
            CustomUser,
            on_delete=models.CASCADE,
            related_name='reviewvotes')
    #slug = models.SlugField(
        #max_length=50, unique=True, null=False, editable=False
    #)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    @property
    def num_votes(self):
        return self.reviewvotes.count()

    @property
    def num_likes(self):
        return self.reviewvotes.filter(vote=1).count()

    @property
    def num_dislikes(self):
        return self.reviewvotes.filter(vote=-1).count()

    @property
    def rating(self):
        if self.num_votes == 0: # No jokes, so rating is 0
            return 0
        r = ReviewVote.objects.filter(review=self).aggregate(average=Avg('vote'))
        # Return the rounded rating.
        return round(5 + (r['average'] * 5), 2)

    @property
    def votes(self):
        result = ReviewVote.objects.filter(review=self).aggregate(
            num_votes=Count('vote'),
            sum_votes=Sum('vote')
        )
        # If there aren't any votes yet, return a dictionary with values of 0.
        if result['num_votes'] == 0:
            return {'num_votes': 0, 'rating': 0, 'likes': 0, 'dislikes': 0}
        # Otherwise, calculate the dict values using num_votes and sum_votes.
        result['rating'] = round(
            5 + ((result['sum_votes']/result['num_votes'])*5), 2
        )
        result['dislikes'] = int((result['num_votes'] - result['sum_votes'])/2)
        result['likes'] = result['num_votes'] - result['dislikes']

        return result

    def get_absolute_url(self):
        return reverse('users:reviewspage')
    #def get_absolute_url(self):
        #return reverse('jokes:detail', args=[self.slug])

    def save(self, *args, **kwargs):
        #if not self.slug:
            #value = str(self)
            #self.slug = unique_slug(value, type(self))

        super().save(*args, **kwargs)

    def __str__(self):
        return self.question

    # def __str__(self):
    #   return str(self.id)

    # def get_review(self):
    #   return self.review

class ReviewVote(models.Model):
    customuser = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE
        #related_name='reviewvotes'
    )
    vote = models.SmallIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    #class Meta:
        #constraints = [
            #models.UniqueConstraint(
                #fields=['user', 'joke'], name='one_vote_per_user_per_joke'
            #)
        #]

    """
    @property
    def num_votes(self):
        return self.reviews.count()

    @property
    def num_likes(self):
        return self.reviews.filter(vote=1).count()

    @property
    def num_dislikes(self):
        return self.reviews.filter(vote=-1).count()

    @property
    def rating(self):
        if self.num_votes == 0: # No reviews, so rating is 0
            return 0

        r = Review.objects.filter(review=self).aggregate(average=Avg('vote'))

        # Return the rounded rating.
        return round(5 + (r['average'] * 5), 2)

    @property
    def votes(self):
        result = Review.objects.filter(review=self).aggregate(
            num_votes=Count('vote'),
            sum_votes=Sum('vote')
        )

        # If there aren't any votes yet, return a dictionary with values of 0.
        if result['num_votes'] == 0:
            return {'num_votes': 0, 'rating': 0, 'likes': 0, 'dislikes': 0}

        # Otherwise, calculate the dict values using num_votes and sum_votes.
        result['rating'] = round(
            5 + ((result['sum_votes']/result['num_votes'])*5), 2
        )
        result['dislikes'] = int((result['num_votes'] - result['sum_votes'])/2)
        result['likes'] = result['num_votes'] - result['dislikes']

        return result

    #def get_absolute_url(self):
        #return reverse('users:reviewspage')

    #def save(self, *args, **kwargs):
        #if not self.slug:
            #value = str(self)
            #self.slug = unique_slug(value, type(self))
        # Call super().save() to do whatever the save() method of models.Model does to save the object:
        #super().save(*args, **kwargs)

    def __str__(self):
        return self.review

    """
    class Meta:
        ordering = ['created']

    #user = models.ForeignKey(
        #settings.AUTH_USER_MODEL, on_delete=models.PROTECT,
        #related_name='reviews'
    #)

    #https://docs.djangoproject.com/en/4.1/ref/models/fields/#django.db.models.DateField.auto_now_add

    #def get_review(self):
        # if customuser.is_validated:
        #return self.game, self.comment, self.customuser, self.created, #self.updated
        # db_table = ['?']
        # order_with_respect_to = ?
        # https://docs.djangoproject.com/en/4.1/ref/models/options/#order-with-respect-to
        # https://docs.djangoproject.com/en/4.1/ref/models/options/#default-permissions
        # -- Defaults to ('add', 'change', 'delete', 'view').


"""
https://blog.devgenius.io/lets-build-a-movie-review-django-app-47658f8e3751
from django.db import models
from django.utils import timezone


class Movie(models.Model):
    title = models.CharField(max_length=40)
    description =  models.TextField(max_length=3000)
    title_upload_date = models.DateTimeField(default=timezone.now)
    movie_cover = models.FileField(upload_to='')

    def __str__(self):
        return self.title


class Review(models.Model):
    author = models.CharField(max_length=40, default="anonymous")
    review_date = models.DateTimeField(default=timezone.now)
    rate_choices = (
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5)
    )
    stars = models.IntegerField(choices=rate_choices)
    comment = models.TextField(max_length=4000)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return self.movie.title
"""


"""
class ProductReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    review_text = models.TextField()
    review_rating = models.CharField(choices=RATING, max_Length=150)

    def get_review_rating(self):
        return self.review_rating
"""

"""
def get_absolute_url(self):
    return reverse('reviews:detail', args=[self.slug])

def save(self, *args, **kwargs):
    if not self.slug:
        value = str(self)
        self.slug = unique_slug(value, type(self))
    super().save(*args, **kwargs)

def __str__(self):
    return self.review
"""

"""
https://medium.com/django-rest/lets-build-a-basic-product-review-backend-with-drf-part-1-652dd9b95485
https://gist.github.com/egitimplus/63cde11b9138c6a6cf85977f0d69c112#file-models-py

class Comment(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments', related_query_name='comment')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', related_query_name='comment')
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
"""

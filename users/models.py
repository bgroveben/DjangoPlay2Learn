
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser

from django.core.exceptions import ValidationError
from django.core.files.images import get_image_dimensions


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
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class CustomUser(AbstractUser):


    dob = models.DateField(
        verbose_name="Date of Birth", null=True, blank=True
    )

    def get_absolute_url(self):
        return reverse('my_account')

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

"""
class ReviewModel(models.Model):
    
    review = Review(
        vote=1,
        comment="comment",
        game="game",
        customuser=CustomUser.objects.first(),
        created=datetime.now(),
        updated=datetime.now())
    

    game = models.TextField(max_length=200)
    comment = models.TextField(max_length=100, blank=True)
    customuser = models.ForeignKey(
            CustomUser,
            on_delete=models.CASCADE)
    slug = models.SlugField(
        max_length=50, unique=True, null=False, editable=False
    )
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
        return reverse('users', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            value = str(self)
            self.slug = unique_slug(value, type(self))
            #self.slug = slugify(value)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.game


    class Meta:
        #managed = False
        db_table = 'users_reviewmodel'
"""
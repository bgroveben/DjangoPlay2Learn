from django.db import models
import datetime


class Game(models.Model):
    id= models.CharField(max_length=20,primary_key=True,serialize=False,
    verbose_name='Game ID')
    game = models.CharField(max_length=200)
    reviewed = models.DateTimeField('date reviewed')

    def save(self,*args, **kwargs):
        # because recursion is divine
        super().save(*args, **kwargs)

    def __str__(self):
        #return self.game
        return str(self.id)

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Review(models.Model):
    #user = models.CharField(max_length=40, default="anonymous")
    #id = models.IntegerField(primary_key=True)
    id= models.CharField(max_length=20,primary_key=True,serialize=False,
    verbose_name='Review ID')
    user = models.CharField(max_length=40)
    # customuser
    #review_date = models.DateTimeField(default=timezone.now())
    rating = (
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5)
    )
    votes = models.IntegerField(choices=rating)
    comment = models.TextField(max_length=4000)
    #game = models.ForeignKey(Game, on_delete=models.CASCADE)
    game = models.ForeignKey('Game', null=True, blank=True,
    on_delete=models.CASCADE)

    def __str__(self):
        # return self.game.title
        # return self.game
        # return self.votes
        return self.comment
        # return self.rating
"""
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

"""

"""
class Game(models.Model):
    title = models.CharField(max_length=40)
    #description =  models.TextField(max_length=3000)
    #title_upload_date = models.DateTimeField(default=timezone.now)
    #movie_cover = models.FileField(upload_to='')

    def __str__(self):
        return self.title



class Reviews(models.Model):
    author = models.CharField(max_length=40, default="anonymous")
    # customuser
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
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    def __str__(self):
        return self.game.title
"""

from django.db import models
import datetime
from django.conf import settings
from users.models import CustomUser
from django.urls import path
#from review.views import ReviewView


class Review(models.Model):

    MATH = "MATH FACTS"
    ANAGRAM = "ANAGRAM HUNT"
    GAME_CHOICES = [
    (MATH, "Math Facts"),
    (ANAGRAM, "Anagram Hunt")
    ]

    RATING = (
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5)
    )
    username = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name='reviews'
    )
    game = models.TextField(choices=GAME_CHOICES, default=MATH)
    votes = models.IntegerField(choices=RATING)
    comment = models.TextField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    #def get_absolute_url(self):
        #return path('/review/', ReviewView.as_view())
        #return '/review/myreviews/'

    def __str__(self):
        #return self.game.title
        return self.game

    class Meta:
        ordering = ["created"]
        verbose_name = 'Review'
        #db_table = 'review'

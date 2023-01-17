from django.db import models
import datetime
from django.conf import settings


class Review(models.Model):

    MATH = "MATH"
    ANAGRAM = "ANAGRAM"
    GAME_CHOICES = [
    (MATH,"Math Game"),
    (ANAGRAM, "Anagram Game")
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
    comment = models.TextField(max_length=3000)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    #def __str__(self):  YAGNI?
        #return self.game.title
        # return self.game

    class Meta:
        ordering = ["created"]
        verbose_name = 'Review'

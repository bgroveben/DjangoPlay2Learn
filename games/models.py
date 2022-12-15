from django.db import models

# Create your models here.
class GameScore(models.Model):

    MATH = "MATH"
    ANAGRAM = "ANAGRAM"

    GAME_CHOICES = [
    (MATH,"Math Game"),
    (ANAGRAM, "Anagram Game")
    ]

    username = models.TextField()
    game = models.TextField(choices=GAME_CHOICES, default=MATH)
    score = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

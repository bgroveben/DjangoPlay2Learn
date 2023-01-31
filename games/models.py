from django.db import models

# ?? from users.models import CustomUser ???

class GameScores(models.Model):

    """
    Add tracking history for both games that stores the time (the time the
    user finished the game), game type (e.g., Math Facts Practice), game
    settings (e.g., operation: multiplication, max number: 20), and final
    score for each game.
    """

    MATH = "MATH FACTS"
    ANAGRAM = "ANAGRAM HUNT"
    GAME_CHOICES = [
    (MATH, "Math Facts"),
    (ANAGRAM, "Anagram Hunt")
    ]
    created = models.DateTimeField(auto_now_add=True) # time, for now
    username = models.TextField() # use ForeignKeyField with string repr?
    score = models.IntegerField()
    operation = models.TextField() # Game settings
    gamelength = models.TextField()
    maxnum = models.TextField() # only needed for math facts
    game = models.TextField(choices=GAME_CHOICES, default=MATH)

    def __str__(self):
        return self.username

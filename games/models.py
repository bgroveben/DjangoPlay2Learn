from django.db import models


class GameScores(models.Model):

    """
    Add tracking history for both games that stores the time (the time 
    the user finished the game), game type (e.g., Math Facts Practice), 
    game settings (e.g., operation: multiplication, max number: 20), and 
    final score for each game.
    """

    MATH = "MATH FACTS"
    ANAGRAM = "ANAGRAM HUNT"
    GAME_CHOICES = [
    (MATH, "Math Facts"),
    (ANAGRAM, "Anagram Hunt")
    ]
    created = models.DateTimeField(auto_now_add=True)
    username = models.TextField()
    score = models.IntegerField()
    operation = models.TextField()
    gamelength = models.TextField()
    maxnum = models.TextField()
    game = models.TextField(choices=GAME_CHOICES, default=MATH)

    def __str__(self):
        return str(self.username)

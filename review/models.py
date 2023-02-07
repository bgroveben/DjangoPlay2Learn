from django.db import models
import datetime
from django.conf import settings
from users.models import CustomUser


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

    def __str__(self):
        #return self.game.title
        return self.game

    class Meta:
        ordering = ["created"]
        verbose_name = 'Review'
        db_table = 'review_reviewmodel'

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
        db_table = 'review_reviewmodel'
"""
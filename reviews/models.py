from django.db import models

from recipes.models import Recipe, Author


class Review(models.Model):
    review = models.TextField()
    rating = models.IntegerField()
    date_submitted = models.DateTimeField()

    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name="reviews",
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name="reviews",
    )

from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=255)


class Category(models.Model):
    category = models.CharField(max_length=255)


class Recipe(models.Model):
    name = models.CharField(max_length=255)
    date_published = models.DateTimeField()
    description = models.TextField()
    calories = models.FloatField()
    fat_content = models.FloatField()
    saturated_fat_content = models.FloatField()
    cholesterol_content = models.FloatField()
    sodium_content = models.FloatField()
    carbohydrate_content = models.FloatField()
    fiber_content = models.FloatField()
    sugar_content = models.FloatField()
    protein_content = models.FloatField()
    recipe_servings = models.IntegerField()
    cook_time = models.DurationField()
    prep_time = models.DurationField()
    total_time = models.DurationField()

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="recipes",
    )

    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name="recipes",
    )


class Keyword(models.Model):
    keyword = models.CharField(max_length=255)
    recipes = models.ManyToManyField(
        Recipe,
        related_name="keywords",
    )

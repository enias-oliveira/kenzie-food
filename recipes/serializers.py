import datetime

from rest_framework import serializers
from .models import Recipe



class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = [
            "id",
            "name",
            "cook_time",
            "prep_time",
            "total_time",
            "date_published",
            "description",
            "calories",
            "fat_content",
            "saturated_fat_content",
            "cholesterol_content",
            "sodium_content",
            "carbohydrate_content",
            "fiber_content",
            "sugar_content",
            "protein_content",
            "recipe_servings",
            "category",
            "author",
        ]


class AuthorRatingRankingSerializer(serializers.ModelSerializer):
    avg_rating = serializers.FloatField(source="average_rating")

    class Meta:
        model = Recipe
        fields = (
            "id",
            "name",
            "avg_rating",
        )


class RecipesCountDailySerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = (
            'date',
            'recipes',
        )


class RecipesCountWeeklySerializer(serializers.ModelSerializer):
    date = serializers.SerializerMethodField('get_first_day_of_week')

    def get_first_day_of_week(self, recipe):
        return datetime.datetime.fromisocalendar(
            year=recipe["year"],
            week=recipe["week"],
            day=1,
        ).date()

    class Meta:
        model = Recipe
        fields = (
            "date",
            "recipes",
        )


class RecipesCountMonthlySerializer(serializers.ModelSerializer):
    date = serializers.SerializerMethodField('get_year_and_month')

    def get_year_and_month(self, recipe):
        return f"{recipe['year']:02}-{recipe['month']:02}"

    class Meta:
        model = Recipe
        fields = (
            "date",
            "recipes",
        )


class RecipesCountYearlySerializer(serializers.ModelSerializer):
    date = serializers.SerializerMethodField('get_year')

    def get_year(self, recipe):
        return recipe["year"]

    class Meta:
        model = Recipe
        fields = (
            "date",
            "recipes",
        )

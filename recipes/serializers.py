from rest_framework import serializers
from .models import Recipe


class ServingsSerializer(serializers.ModelSerializer):
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

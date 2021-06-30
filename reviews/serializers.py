from rest_framework import serializers
from recipes.models import Recipe


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = [
            "id",
            "name",
            "date_published",
            "description",
            "category",
            "author",
            "total_reviews",
            "average_rating",
        ]
        depth = 2

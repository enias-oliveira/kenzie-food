from rest_framework.viewsets import ReadOnlyModelViewSet
from django.db.models import Count, Avg

from recipes.models import Recipe
from .serializers import ReviewSerializer


class ReviewViewSet(ReadOnlyModelViewSet):
    queryset = (
        Recipe.objects.only(
            "id",
            "name",
            "date_published",
            "description",
            "category",
            "author",
        )
        .prefetch_related(
            "category",
            "author",
            "reviews",
        )
        .annotate(Count("reviews"), Avg("reviews__rating"))
        .order_by("name")
    )

    serializer_class = ReviewSerializer

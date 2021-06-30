from rest_framework.viewsets import ReadOnlyModelViewSet

from recipes.models import Recipe
from .serializers import ReviewSerializer


class ReviewViewSet(ReadOnlyModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = ReviewSerializer

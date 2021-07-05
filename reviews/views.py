from rest_framework.viewsets import ReadOnlyModelViewSet

from django.db.models import Count, Avg
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from silk.profiling.profiler import silk_profile

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
        .annotate(
            total_reviews=Count("reviews"),
            average_rating=Avg(
                "reviews__rating",
            ),
        )
        .prefetch_related(
            "category",
            "author",
            "reviews",
        )
    )
    serializer_class = ReviewSerializer

    @method_decorator(cache_page(600))
    @silk_profile(name='Reviews List')
    def list(self, request, *args, **kwargs):
        return super(ReviewViewSet, self).list(request, *args, **kwargs)

    @method_decorator(cache_page(600))
    @silk_profile(name='Reviews Retrieve')
    def retrieve(self, request, *args, **kwargs):
        return super(ReviewViewSet, self).retrieve(request, *args, **kwargs)

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from django.db.models import Avg, Count
from django.db.models.functions import ExtractWeek, ExtractYear, ExtractMonth
from django.db.models.functions import TruncDate

from rest_framework.viewsets import ReadOnlyModelViewSet

from silk.profiling.profiler import silk_profile

from recipes.models import Recipe

from .serializers import (
    RecipeSerializer,
    AuthorRatingRankingSerializer,
    RecipesCountDailySerializer,
    RecipesCountWeeklySerializer,
    RecipesCountMonthlySerializer,
    RecipesCountYearlySerializer,
)


class ServingsViewSet(ReadOnlyModelViewSet):
    queryset = (
        Recipe.objects.all()
        .prefetch_related("category", "author")
        .order_by("-recipe_servings")
    )
    serializer_class = RecipeSerializer

    @method_decorator(cache_page(600))
    @silk_profile(name="Servings List")
    def list(self, request, *args, **kwargs):
        return super(ServingsViewSet, self).list(request, *args, **kwargs)

    @method_decorator(cache_page(600))
    @silk_profile(name="Servings Retrieve")
    def retrieve(self, request, *args, **kwargs):
        return super(ServingsViewSet, self).retrieve(request, *args, **kwargs)


class YearViewSet(ReadOnlyModelViewSet):
    serializer_class = RecipeSerializer

    def get_queryset(self):
        year = int(self.kwargs["year"])
        return Recipe.objects.filter(
            date_published__year=year,
        ).prefetch_related("category", "author")

    @method_decorator(cache_page(600))
    @silk_profile(name="Year List")
    def list(self, request, *args, **kwargs):
        return super(YearViewSet, self).list(request, *args, **kwargs)


class RecipeRangeViewSet(ReadOnlyModelViewSet):
    serializer_class = RecipeSerializer
    field_name = None

    def get_queryset(self):
        min = float(self.request.query_params.get("min"))
        max = float(self.request.query_params.get("max"))

        range_filter = {
            f"{self.field_name}__range": (
                min,
                max,
            )
        }

        return Recipe.objects.filter(**range_filter).prefetch_related(
            "category",
            "author",
        )

    @method_decorator(cache_page(600))
    @silk_profile(name=f"{field_name} List")
    def list(self, request, *args, **kwargs):
        return super(RecipeRangeViewSet, self).list(request, *args, **kwargs)


class CaloriesViewSet(RecipeRangeViewSet):
    field_name = "calories"


class FatContentViewSet(RecipeRangeViewSet):
    field_name = "fat_content"


class SaturatedFatContentViewSet(RecipeRangeViewSet):
    field_name = "saturated_fat_content"


class AuthorRatingRankingViewSet(ReadOnlyModelViewSet):
    serializer_class = AuthorRatingRankingSerializer
    queryset = (
        Recipe.objects.all()
        .prefetch_related("author", "reviews")
        .annotate(average_rating=Avg("reviews__rating"))
        .order_by(
            "-average_rating",
        )
    )


class RecipesCountDailyViewSet(ReadOnlyModelViewSet):
    serializer_class = RecipesCountDailySerializer
    queryset = (
        Recipe.objects.annotate(date=TruncDate("date_published"))
        .values("date")
        .annotate(recipes=Count("id"))
    )

    @method_decorator(cache_page(600))
    def list(self, request, *args, **kwargs):
        return super(RecipesCountDailyViewSet, self).list(request, *args, **kwargs)


class RecipesCountWeeklyViewSet(ReadOnlyModelViewSet):
    serializer_class = RecipesCountWeeklySerializer
    queryset = (
        Recipe.objects.annotate(
            year=ExtractYear("date_published"),
            week=ExtractWeek("date_published"),
        )
        .values("year", "week")
        .annotate(recipes=Count("id"))
        .order_by("year", "week")
    )

    @method_decorator(cache_page(600))
    def list(self, request, *args, **kwargs):
        return super(RecipesCountWeeklyViewSet, self).list(request, *args, **kwargs)


class RecipesCountMonthlyViewSet(ReadOnlyModelViewSet):
    serializer_class = RecipesCountMonthlySerializer
    queryset = (
        Recipe.objects.annotate(
            year=ExtractYear("date_published"),
            month=ExtractMonth("date_published"),
        )
        .values("year", "month")
        .annotate(recipes=Count("id"))
        .order_by("year", "month")
    )

    @method_decorator(cache_page(600))
    def list(self, request, *args, **kwargs):
        return super(RecipesCountMonthlyViewSet, self).list(request, *args, **kwargs)


class RecipesCountYearlyViewSet(ReadOnlyModelViewSet):
    serializer_class = RecipesCountYearlySerializer
    queryset = (
        Recipe.objects.annotate(
            year=ExtractYear("date_published"),
        )
        .values("year")
        .annotate(recipes=Count("id"))
        .order_by("year")
    )

    @method_decorator(cache_page(600))
    def list(self, request, *args, **kwargs):
        return super(RecipesCountYearlyViewSet, self).list(request, *args, **kwargs)

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from rest_framework.viewsets import ReadOnlyModelViewSet

from silk.profiling.profiler import silk_profile

from recipes.models import Recipe

from .serializers import RecipeSerializer


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


class CaloriesViewSet(ReadOnlyModelViewSet):
    serializer_class = RecipeSerializer

    def get_queryset(self):
        min = float(self.request.query_params.get("min"))
        max = float(self.request.query_params.get("max"))

        return Recipe.objects.filter(calories__range=(min, max)).prefetch_related(
            "category",
            "author",
        )

    @method_decorator(cache_page(600))
    @silk_profile(name="Calories List")
    def list(self, request, *args, **kwargs):
        return super(CaloriesViewSet, self).list(request, *args, **kwargs)

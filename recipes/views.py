from rest_framework.viewsets import ReadOnlyModelViewSet

# from django.utils.decorators import method_decorator
# from django.views.decorators.cache import cache_page

# from silk.profiling.profiler import silk_profile

from recipes.models import Recipe
from .serializers import ServingsSerializer


class ServingsViewSet(ReadOnlyModelViewSet):
    queryset = Recipe.objects.all().order_by("-recipe_servings")
    serializer_class = ServingsSerializer

from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import ServingsViewSet, YearViewSet, CaloriesViewSet

from reviews.urls import reviews_router

servings_router = DefaultRouter()
servings_router.register(r"servings", ServingsViewSet, basename="servings")

calories_router = DefaultRouter()
calories_router.register(r"calories", CaloriesViewSet, basename="calories")

urlpatterns = [
    path("recipes/", include(reviews_router.urls)),
    path("recipes/", include(servings_router.urls)),
    path("recipes/year/<int:year>/", YearViewSet.as_view({"get": "list"})),
    path("recipes/", include(calories_router.urls)),
]

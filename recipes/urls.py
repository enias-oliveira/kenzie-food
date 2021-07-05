from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import (
    ServingsViewSet,
    YearViewSet,
    CaloriesViewSet,
    FatContentViewSet,
    SaturatedFatContentViewSet,
    AuthorRatingRankingViewSet,
    RecipesCountDailyViewSet,
    RecipesCountWeeklyViewSet,
    RecipesCountMonthlyViewSet,
    RecipesCountYearlyViewSet,
)

from reviews.urls import reviews_router

servings_router = DefaultRouter()
servings_router.register(r"servings", ServingsViewSet, basename="servings")

calories_router = DefaultRouter()
calories_router.register(r"calories", CaloriesViewSet, basename="calories")

fat_content_router = DefaultRouter()
fat_content_router.register(
    r"fat_content",
    FatContentViewSet,
    basename="fat_content",
)

saturated_fat_content_router = DefaultRouter()
saturated_fat_content_router.register(
    r"saturated_fat_content",
    SaturatedFatContentViewSet,
    basename="saturated_fat_content",
)

author_rating_ranking_router = DefaultRouter()
author_rating_ranking_router.register(
    r"author_rating_ranking",
    AuthorRatingRankingViewSet,
    basename="author_rating_ranking",
)


urlpatterns = [
    path("recipes/", include(reviews_router.urls)),
    path("recipes/", include(servings_router.urls)),
    path("recipes/year/<int:year>/", YearViewSet.as_view({"get": "list"})),
    path("recipes/", include(calories_router.urls)),
    path("recipes/", include(fat_content_router.urls)),
    path("recipes/", include(saturated_fat_content_router.urls)),
    path("recipes/", include(author_rating_ranking_router.urls)),
    path(
        "recipes/recipes_count/daily/",
        RecipesCountDailyViewSet.as_view({"get": "list"}),
    ),
    path(
        "recipes/recipes_count/weekly/",
        RecipesCountWeeklyViewSet.as_view({"get": "list"}),
    ),
    path(
        "recipes/recipes_count/monthly/",
        RecipesCountMonthlyViewSet.as_view({"get": "list"}),
    ),
    path(
        "recipes/recipes_count/yearly/",
        RecipesCountYearlyViewSet.as_view({"get": "list"}),
    ),
]

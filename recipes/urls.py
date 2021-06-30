from django.urls import path, include

from reviews.urls import reviews_router

urlpatterns = [path("recipes/", include(reviews_router.urls))]

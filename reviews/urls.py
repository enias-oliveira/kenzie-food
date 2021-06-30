from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ReviewViewSet

reviews_router = DefaultRouter()
reviews_router.register(r"reviews", ReviewViewSet, basename="reviews")

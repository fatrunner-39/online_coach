from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ProfileListCreateView, ProfileDetailView


urlpatterns = [
    path("profiles/", ProfileListCreateView.as_view(), name="profiles"),
    path("profile/<int:pk>/", ProfileDetailView.as_view(), name="profile"),
]

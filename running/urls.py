from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ReportViewSet, WorkoutViewSet


router = DefaultRouter()
router.register('workouts', WorkoutViewSet)
router.register('reports', ReportViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

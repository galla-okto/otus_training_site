from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import WorkoutViewSet, TrainerViewSet

router = DefaultRouter()
router.register('trainers', TrainerViewSet)
router.register('workouts', WorkoutViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]

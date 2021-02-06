from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import WorkoutViewSet, TrainerViewSet, ScheduleViewSet

router = DefaultRouter()
router.register('trainers', TrainerViewSet)
router.register('workouts', WorkoutViewSet)
router.register('schedules', ScheduleViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]

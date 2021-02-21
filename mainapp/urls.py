from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import WorkoutViewSet, TrainerViewSet, ScheduleViewSet, ClientViewSet, EnrollmentViewSet

router = DefaultRouter()
router.register('trainers', TrainerViewSet)
router.register('workouts', WorkoutViewSet)
router.register('schedules', ScheduleViewSet)
router.register('clients', ClientViewSet)
router.register('enrollments', EnrollmentViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]

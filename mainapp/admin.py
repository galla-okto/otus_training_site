from django.contrib import admin
from django.db.models import F

from .models import Trainer, Workout, Schedule

@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'position', 'email'
    list_display_links = 'name',

@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'description', 'price', 'duration_lesson', 'quantity_lesson', 'initial_level', 'star_rating'
    list_display_links = 'name',

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(ScheduleAdmin, self).get_queryset(request)
        return qs.annotate(workout_name=F("workout__name"))

    def workoutname(self, obj: Schedule):
        return obj.workout_name

    list_display = 'id', 'title', 'date_time_start', 'date_time_end', 'workoutname', 'trainer'
    list_display_links = 'title',

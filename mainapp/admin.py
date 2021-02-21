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
        qs = super().get_queryset(request)
        return qs.annotate(workoutname=F("workout__name"), trainername=F("trainer__name"))

    def workoutname(self, obj: Schedule):
        return obj.workoutname

    def trainername(self, obj: Trainer):
        return obj.trainername

    list_display = 'id', 'title', 'date_time_start', 'date_time_end', 'workoutname', 'trainername'
    list_display_links = 'title',

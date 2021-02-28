from django.contrib import admin
from django.db.models import F

from .models import Trainer, Workout, Schedule, Client, Enrollment


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
        return qs.annotate(workoutlevel=F("workout__initial_level"), trainername=F("trainer__name"))

    def workoutlevel(self, obj: Schedule):
        return obj.workoutlevel

    def trainername(self, obj: Trainer):
        return obj.trainername

    list_display = 'id', 'title', 'date_time_start', 'date_time_end', 'workoutlevel', 'trainername'
    list_display_links = 'title',


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = 'id', 'nick', 'user', 'email'
    list_display_links = 'nick',


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = 'id', 'client', 'schedule'
    list_display_links = 'id',

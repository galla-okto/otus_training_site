from django.contrib import admin

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
    def get_workoutlevel(self, obj):
        return obj.workout.initial_level

    def get_trainername(self, obj):
        return obj.trainer.name

    list_display = 'id', 'title', 'date_time_start', 'date_time_end', 'get_workoutlevel', 'get_trainername'
    list_display_links = 'title',


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = 'id', 'nick', 'user', 'email'
    list_display_links = 'nick',


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = 'id', 'client', 'schedule'
    list_display_links = 'id',

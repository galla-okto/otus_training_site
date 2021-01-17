from django.contrib import admin

from .models import Trainer, Workout, Schedule

@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'position', 'email'
    list_display_links = 'name',

@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = 'id', 'name'
    list_display_links = 'name',

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = 'id', 'title', 'date_start', 'time_start', 'date_end', 'time_end', 'workout', 'trainer'
    list_display_links = 'title',
from django.contrib import admin

from .models import Trainer, Workout, Schedule

@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'position', 'email'
    list_display_links = 'name',

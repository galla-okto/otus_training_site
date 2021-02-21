from rest_framework import serializers
from .models import Trainer, Workout, Schedule, Client, Enrollment


class TrainerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Trainer
        fields = 'id', 'name', 'email', 'position', 'data'


class WorkoutSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Workout
        fields = 'id', 'name', 'description', 'price', 'duration_lesson', 'quantity_lesson', 'initial_level', \
                 'star_rating'


class ScheduleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Schedule
        fields = 'id', 'title', 'date_time_start', 'date_time_end', 'workout', 'workout_id', 'trainer', 'trainer_id'


class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = 'id', 'nick'


class EnrollmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Enrollment
        fields = 'id', 'client', 'schedule'

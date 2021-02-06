from rest_framework import serializers
from .models import Trainer, Workout


class TrainerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Trainer
        fields = 'id', 'name', 'email', 'position', 'data'


class WorkoutSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Workout
        fields = 'id', 'name', 'description', 'price', 'duration_lesson', 'quantity_lesson', 'initial_level', 'star_rating'

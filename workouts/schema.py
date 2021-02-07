import graphene
from graphene_django import DjangoObjectType

from mainapp.models import Trainer, Workout, Schedule


class TrainerType(DjangoObjectType):
    class Meta:
        model = Trainer
        fields = ('id', 'name', 'email', 'position', 'data')


class WorkoutType(DjangoObjectType):
    class Meta:
        model = Workout
        fields = ('id', 'name', 'description', 'price', 'duration_lesson', 'quantity_lesson', 'initial_level', 'star_rating')


class ScheduleType(DjangoObjectType):
    class Meta:
        model = Schedule
        fields = ('id', 'title', 'date_time_start', 'date_time_end', 'workout', 'trainer')


class Query(graphene.ObjectType):
    all_schedules = graphene.List(ScheduleType)
    all_workouts = graphene.List(WorkoutType)
    all_trainers = graphene.List(TrainerType)

    def resolve_all_schedules(self, info):
        return Schedule.objects.all()

    def resolve_all_workouts(self, info):
        return Workout.objects.all()

    def resolve_all_trainers(self, info):
        return Trainer.objects.all()


schema = graphene.Schema(query=Query)

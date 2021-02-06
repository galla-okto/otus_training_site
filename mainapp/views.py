from django.views.generic import DetailView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.viewsets import ModelViewSet

from mainapp.models import Workout, Trainer, Schedule
from mainapp.mixins import PageNameMixin
from .serializers import WorkoutSerializer, TrainerSerializer, ScheduleSerializer


class WorkoutListView(PageNameMixin, APIView):
    page_name = 'тренировки'

    def get(self, request):
        items = Workout.objects.all()
        serializer = WorkoutSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WorkoutSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WorkoutDetailView(PageNameMixin, DetailView):
    page_name = 'тренировка'

    def get(self, request, pk):
        item = get_object_or_404(Workout, pk=pk)
        serializer = WorkoutSerializer(item)
        return Response(serializer.data)


class TrainerViewSet(ModelViewSet):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer


class WorkoutViewSet(ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer


class ScheduleViewSet(ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

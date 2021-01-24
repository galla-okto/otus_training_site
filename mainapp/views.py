from django.shortcuts import render

from mainapp.models import Workout


def index(request):
    workouts = Workout.objects.all()
    context = {
        'page_name': 'главная',
        'workouts': workouts,
    }
    return render(request, 'mainapp/index.html', context)

from django.shortcuts import render, get_object_or_404

from mainapp.models import Workout


def index(request):
    workouts = Workout.objects.all()
    context = {
        'page_name': 'главная',
        'workouts': workouts,
    }
    return render(request, 'mainapp/index.html', context)


def about(request):
    return render(request, 'mainapp/about.html')


def workout(request, pk):
    workout = get_object_or_404(Workout, pk=pk)
    # try:
    #     workout = Workout.objects.get(pk=pk)
    # except Exception as e:
    #     return
    # workout = Workout.objects.filter(pk=pk).first()
    context = {
        'workout': workout
    }
    return render(request, 'mainapp/workout.html', context)

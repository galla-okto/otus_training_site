from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView

from mainapp.models import Workout


class PageNameMixin:
    page_name = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = self.page_name
        return context


# def index(request):
#     workouts = Workout.objects.all()
#     context = {
#         'page_name': 'главная',
#         'workouts': workouts,
#     }
#     return render(request, 'mainapp/index.html', context)


class WorkoutListView(PageNameMixin, ListView):
    model = Workout
    page_name = 'тренировки'
    # paginate_by = 15

# def about(request):
#     return render(request, 'mainapp/about.html')


# def workout(request, workout_pk):
#     workout = get_object_or_404(Workout, pk=pk)
#     # try:
#     #     workout = Workout.objects.get(pk=pk)
#     # except Exception as e:
#     #     return
#     # workout = Workout.objects.filter(pk=pk).first()
#     context = {
#         'workout': workout
#     }
#     return render(request, 'mainapp/workout.html', context)


# class WorkoutDetailView(DetailView):
#     model = Workout
#     template_name = 'mainapp/workout.html'
#     pk_url_kwarg = 'workout_pk'
#     context_object_name = 'workout'


class WorkoutDetailView(PageNameMixin, DetailView):
    model = Workout
    page_name = 'тренировка'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['page_name'] = 'тренировка'
    #     return context


class WorkoutCreateView(CreateView):
    model = Workout
    fields = '__all__'
    success_url = reverse_lazy('mainapp:index')

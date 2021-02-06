from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from mainapp.models import Workout

from mainapp.mixins import PageNameMixin


class WorkoutListView(PageNameMixin, ListView):
    model = Workout
    page_name = 'тренировки'


class WorkoutDetailView(PageNameMixin, DetailView):
    model = Workout
    page_name = 'тренировка'


class WorkoutCreateView(CreateView):
    model = Workout
    fields = '__all__'


class WorkoutUpdateView(UpdateView):
    model = Workout
    fields = '__all__'
    template_name_suffix = '_update_form'


class WorkoutDeleteView(DeleteView):
    model = Workout
    success_url = reverse_lazy('mainapp:index')

from django.urls import path
from django.views.generic import TemplateView

import mainapp.views as views

app_name = 'mainapp'

urlpatterns = [
    # path('', views.index, name='index'),
    path('',
         views.WorkoutListView.as_view(),
         name='index'),

    # path('about/', views.about, name='about'),
    path('about/',
         TemplateView.as_view(template_name='mainapp/about.html'),
         name='about'),

    # path('workout/<int:workout_pk>/', views.workout, name='workout'),
    path('workout/<int:pk>/',
         views.WorkoutDetailView.as_view(),
         name='workout'),

    path('workout/add/',
         views.WorkoutCreateView.as_view(),
         name='workout-add'),
]

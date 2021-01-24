from django.urls import path

import mainapp.views as views

app_name = 'mainapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('workout/<int:pk>/', views.workout, name='workout'),
]

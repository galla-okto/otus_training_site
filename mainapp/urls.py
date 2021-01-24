from django.urls import path
from django.views.generic import TemplateView

import mainapp.views as views

app_name = 'mainapp'

urlpatterns = [
    path('', views.index, name='index'),

    # path('about/', views.about, name='about'),
    path('about/',
         TemplateView.as_view(template_name='mainapp/about.html'),
         name='about'),

    path('workout/<int:pk>/', views.workout, name='workout'),
]

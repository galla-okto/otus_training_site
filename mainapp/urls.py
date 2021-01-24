from django.urls import path

import mainapp.views as views

app_name = 'mainapp'

urlpatterns = [
    path('', views.index, name='index'),
]

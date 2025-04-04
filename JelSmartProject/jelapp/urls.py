from django.urls import path
from . import views

app_name = 'jelapp'  # Namespace definiálása

urlpatterns = [
    path('', views.home, name='home'),
    path('kezikonyvek/', views.kezikonyvek, name='kezikonyvek'),
    path('gyakorlok/', views.gyakorlok, name='gyakorlok'),
    path('fogalmak/', views.fogalmak, name='fogalmak'),
    path('resztudas/', views.resztudas, name='resztudas')
]

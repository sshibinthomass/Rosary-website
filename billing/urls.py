from django.urls import path

from . import views

app_name = 'billing'

urlpatterns = [
    path('plantfinder', views.plantfinder,name='plantfinder'),
    path('plantlist',views.plantlist,name='plantlist'),
    path('local',views.local,name='local'),
]

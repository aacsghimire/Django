from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Blog-Home'),
    path('abouta/', views.about,name='Blog-About'),
]
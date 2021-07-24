from django.urls import path
from . import views

urlpatterns = [
    path('', views.randomWord),
    path('/restart', views.restart),
]
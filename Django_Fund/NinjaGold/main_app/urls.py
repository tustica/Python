from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage),
    path('submitgoal', views.submitgoal),
    path('process', views.process_money),
    path('restart', views.restart),
    path('youwon', views.youwon),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.displayForm),
    path('result', views.result),
]
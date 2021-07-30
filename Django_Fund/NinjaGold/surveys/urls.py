from django.urls import path
from . import views

urlpatterns = [
    path('', views.placeholder),
    path('/new', views.new),
]
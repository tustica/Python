from django.shortcuts import render, HttpResponse, HttpResponseRedirect

def index(request):
    return HttpResponse("Welcome to Dojo and Ninjas")


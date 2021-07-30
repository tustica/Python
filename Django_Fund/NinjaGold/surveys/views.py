from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect

def placeholder(request):
    return HttpResponse("Placeholder to display a list of surveys")

def new(request):
    return HttpResponse("placeholder to create a new survey")
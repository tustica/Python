from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect

def placeholder(request):
    return HttpResponse("Placeholder to later display a list of blogs")

def newBlog(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
    return redirect('/')

def show(request, number):
    return HttpResponse(f"Placeholder to display blog number: {number}")

def edit(request, number):
    return HttpResponse(f"Placeholder to edit blog number: {number}")

def destroy(request, number):
    return redirect('/')

# Create your views here.

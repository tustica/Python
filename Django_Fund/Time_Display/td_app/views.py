from django.shortcuts import render, HttpResponse
from time import gmtime, strftime

def displayTime(request):
    context = {
        "time": strftime("%B %d, %Y %I:%M %p")
    }
    return render(request, 'index.html', context)




from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
import random
from django.utils.crypto import get_random_string

def restart(request):
    if request.method == "GET":
        request.session['randWord'] = ""
        request.session['rwd'] = 0
        return HttpResponseRedirect('/random')
def randomWord(request):
    if request.method == "GET":
        return render(request, 'randomword.html')
    if request.method == "POST":
        WORDS = ("python", "jumble", "easy", "difficult", "answer",  "xylophone", "noble", "weirdo", "zachary")
        word = get_random_string(length=14)
        request.session['randWord'] = word
        request.session['rwd']+=1
        return redirect('/random')



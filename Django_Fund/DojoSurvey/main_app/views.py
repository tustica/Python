from django.shortcuts import render, redirect, HttpResponse

def displayForm(request):
    if request.method == "GET":
        return render(request, 'index.html')
    if request.method == "POST":
        return redirect('survey/result')
    

def result(request):
    if request.method == "GET":
        return render(request, 'success.html')
    if request.method == "POST":
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST.getlist('language')
        request.session['comment'] = request.POST['comment']
        
        return redirect('/result')

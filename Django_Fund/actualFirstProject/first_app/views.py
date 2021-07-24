from django.shortcuts import render, HttpResponse, redirect

def default(request):
    return HttpResponse("placeholder to later display a list of all blogs")

def new(request):
    return HttpResponse("this is the placeholder for all new forms on the blogs")

def create(request):
    return redirect("/")

def show(request, number):
    return HttpResponse(f"placeholder to display blog number : {number}")

def edit(request, number):
    return HttpResponse(f"placeholder to display blog: {number}")

def destroy(request, number):
    return redirect('/')
    
def htmlname(request, name):
    context = {
        "htmlname": name,
        "name": "Noelle",
        "favorite_color": "turquoise",
        "pets": ["Bruce", "Fitz", "Georgie"]
    }
    return render(request, "helloname.html", context)


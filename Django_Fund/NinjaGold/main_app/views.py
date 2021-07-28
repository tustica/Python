from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
import random
from time import gmtime, strftime

def homepage(request):
    if 'gold_amount' not in request.session:
        request.session['gold_amount'] = 0
        request.session['activity_list'] = []
    return render(request, 'index.html')

def submitgoal(request):
    if request.method == "POST":
        request.session['gold_goal'] = request.POST['gold_goal']
    return redirect('/')

def process_money(request):
    if 'farm' in request.POST:
        farm_gold_increase = random.randrange(10, 20, 1)
        request.session['gold_amount']+= farm_gold_increase
        message = "Earned "+str(farm_gold_increase)+" gold from the farm! "+strftime("(%Y/%m/%d %#I:%M %p)")
        result = "add"
    elif 'cave' in request.POST:
        cave_gold_increase = random.randrange(5, 10, 1)
        request.session['gold_amount']+= cave_gold_increase
        message = "Earned "+str(cave_gold_increase)+" gold from the cave "+strftime("(%Y/%m/%d %#I:%M %p)")
        result = "add"
    elif 'house' in request.POST:
        house_gold_increase = random.randrange(2, 5, 1)
        request.session['gold_amount']+= house_gold_increase
        message = "Earned "+str(house_gold_increase)+" gold from the house! "+strftime("(%Y/%m/%d %#I:%M %p)")
        result = "add"
    elif 'casino' in request.POST:
        add_or_subtract = random.choice([True, False])
        if add_or_subtract == True:
            request.session['gold_amount']+=50
            message = "Earned 50 gold from the casino! "+strftime("(%Y/%m/%d %#I:%M %p)")
            result = "add"
        if add_or_subtract == False:
            request.session['gold_amount']-=50
            message = "Lost 50 gold from the casino!!"+strftime("(%Y/%m/%d %#I:%M %p)")
            result = "lost"
    request.session['activity_list'].append({"message": message, "result": result})
        
    if (request.session['gold_amount']) > int(request.session['gold_goal']):
        return redirect('/youwon')
    return redirect('/')

def youwon(request):
    return render(request, 'start.html')

def restart(request):
    request.session.flush()
    return redirect('/')
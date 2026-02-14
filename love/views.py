from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def yes_page(request):
    return render(request, 'yes.html')

def final_page(request):
    return render(request, 'final.html')
def sorry_page(request):
    return render(request, 'sorry.html')
def fights(request):
    return render(request, 'fights.html')

def love_everyday(request):
    return render(request, 'love_everyday.html')
def mood_swings(request):
    return render(request, 'moodswings.html')
def final_promise(request):
    return render(request, "final_promise.html")    
def journey(request):
    return render(request, "journey.html")
def next1(request):
    return render(request, "next1.html") 
def proposal(request):
    return render(request, "proposal.html")       

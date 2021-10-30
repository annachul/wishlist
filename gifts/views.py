from django.shortcuts import render

# Create your views here.

def index(request):
    gifts = [
        {"title":  "First gift"},
        {"title":  "Second gift"}
    ]
    return render(request,'gifts/index.html', {
        "gifts":gifts
    })
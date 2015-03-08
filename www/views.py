from django.shortcuts import render

# Create your views here.

def home(request):
    cd = {}
    return render(request, 'www/home.html', cd)

def cal(request):
    cd = {}
    return render(request, 'www/cal.html', cd)


from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'base/home.html')

def about(request):
    return render(request, 'base/home.html')

def projects(request):
    return render(request, 'base/home.html')

def contact(request):
    return render(request, 'base/home.html')
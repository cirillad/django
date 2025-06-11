from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    # return HttpResponse("Hello app")
    return render(request, 'home.html')

def about(request):
    # return HttpResponse("Hello app")
    return render(request, 'about.html')
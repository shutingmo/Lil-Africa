from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

def homepage(request):
    return render(request, 'django_africa/homePage.html')
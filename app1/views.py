from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def view11(request):
    return HttpResponse("<h1>This is my first line</h1>")

def view12(request):
    return HttpResponse("<h1>This is my second line<h1>")


from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def view21(request):
    return HttpResponse("<h1>This is my 2nd view first line</h1>")

def view22(request):
    return HttpResponse("<h1>This is my 2nd view second line</h1>")
from django.shortcuts import render

# Create your views here.
# core/views.py
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello, World!")
from django.http import HttpResponse
from django.shortcuts import render

def HomePageView(request, *args, **kwargs):
    return HttpResponse("<h1>Hello World</h1>")
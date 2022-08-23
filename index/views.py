from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse



def index(request):
    third = '<h1>Third project</h1>'
    return HttpResponse(third)
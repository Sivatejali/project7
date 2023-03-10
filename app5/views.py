from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def india(request):
    return HttpResponse('<h1>i am indian</h1>')

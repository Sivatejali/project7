from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def sivateja(request):
    return HttpResponse('<h1><marquee>sivateja chowdary lingutla</h1></marquee>')

from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    return HttpResponse('about')

def homepage(request):
    return HttpResponse('homepage')


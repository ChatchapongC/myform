from django.http import HttpResponse
from django.shortcuts import render,redirect

def about(request):
    return HttpResponse('about')

def homepage(request):
    return HttpResponse('homepage')

def index_view(request):
    return render(request, 'index/index.html')


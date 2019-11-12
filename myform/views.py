from django.shortcuts import render
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'registration/#1login.html'

class EventListView(TemplateView):
    template_name = 'myform/index.html'

class SignupView(TemplateView):
    template_name = 'registration/#2signup.html'

class CreateEventView(TemplateView):
    template_name = 'myform/evenlist.html'

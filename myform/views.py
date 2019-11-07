from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.views.generic import TemplateView
from django.views import generic, View
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .form import RegisterForm


class HomeView(TemplateView):
    template_name = 'registration/login.html'


# class RegisterView(TemplateView):
#     template_name = 'registration/registration_form.html'


def create(request):
    return render(request, 'myform/index.html')


def user_login(request):
    """
    If the user is not authenticated, get user's request and execute login.
    """
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('myform:create'))
        else:
            messages.error(request, 'Wrong username or password try again!')
            return render(request, 'registration/login.html')
    else:
        return render(request, 'registration/login.html')


def user_register(request):
    registered = False
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            form = form.save()
            form.set_password(form.password)
            form.save()
            registered = True
            return HttpResponseRedirect(reverse('myform:home'))
    else:
        form = RegisterForm()
    context = {'form': form,
               'registered': registered}
    return render(request, 'registration/registration_form.html', context)

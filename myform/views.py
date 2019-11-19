from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.views import generic, View
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, EvaluateForm
from .models import Event


class HomeView(TemplateView):
    template_name = 'registration/login.html'


class CreateProjectView(TemplateView):
    template_name = 'myform/projectlist.html'


def create_form(request):
    if request.method == 'POST':
        project_form = EvaluateForm(data=request.POST)
        if project_form.is_valid():
            project_form = project_form.save()
        return HttpResponseRedirect(reverse('myform:event'))
    else:
        project_form = EvaluateForm()
    context = {'project_form': project_form}
    return render(request, 'myform/createform.html', context)


class IndexView(generic.ListView):
    model = Event
    template_name = 'myform/index.html'
    context_object_name = 'event_list'

    def get_queryset(self):
        return Event.objects.all()


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
            return HttpResponseRedirect(reverse('myform:event'))
        else:
            messages.error(request, 'Wrong username or password try again!')
            return render(request, 'registration/login.html')
    else:
        return render(request, 'registration/login.html')


def logout_user(request):
    """
    Function to logout user and redirect to login page.
    """
    logout(request)
    return HttpResponseRedirect('/login')


def user_register(request):
    registered = False
    if request.method == 'POST':
        user = UserRegistrationForm(data=request.POST)
        if user.is_valid():
            user = user.save()
            user.set_password(user.password)
            user.save()
            registered = True
            return HttpResponseRedirect(reverse('myform:home'))
    else:
        user = UserRegistrationForm()
    context = {'user': user,
               'registered': registered}
    return render(request, 'registration/registration_form.html', context)

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, FormView
from django.contrib.auth.models import User
from django.views import generic, View
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, EventForm, AddQuestion
from .models import Event, Question
import datetime


class HomeView(TemplateView):
    template_name = 'registration/login.html'


class CreateProjectView(TemplateView):
    template_name = 'myform/projectlist.html'


def evaluator_view(request, event_id):
    question_list = Question.objects.filter(event_id=event_id)
    event = Event.objects.get(id=event_id)
    context = {'question_list': question_list,
               'event': event}
    return render(request, 'myform/evaluator.html', context)


def event_delete(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.user == event.owner:
        event.delete()
    return redirect('myform:event')


def create_event(request):
    if request.method == 'POST':
        event_form = EventForm(request.POST)
        if event_form.is_valid():
            event_form = event_form.save(commit=False)
            event_form.owner = request.user
            event_form.save()
            print(event_form.owner)
            messages.success(
                request, "Event added successfully",
                extra_tags='alert alert-success alert-dismissible fade show')
        else:
            messages.error(
                request, event_form.errors)
        return HttpResponseRedirect(reverse('myform:event'))
    else:
        event_form = EventForm()
        question_form = AddQuestion()
    context = {'event_form': event_form,
               'question_form': question_form}
    return render(request, 'myform/createform.html', context)


def event_edit(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    print(event.owner, event.event_name, event.id)
    if request.user != event.owner:
        return redirect('event')
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid:
            form.save()
        return HttpResponseRedirect(reverse('myform:event'))
    else:
        form = EventForm(instance=event)
    context = {'event_form': form,
               'event': event}
    return render(request, "myform/createform.html", context)


def create_question(request):
    if request.method == 'POST':
        question_form = AddQuestion(request.POST)
        if question_form.is_valid():
            question_form.save()
            messages.success(
                request, "Question added successfully",
                extra_tags='alert alert-success alert-dismissible fade show')
        else:
            messages.error(
                request, question_form.errors)
        return HttpResponseRedirect(reverse('myform:create'))
    else:
        question_form = AddQuestion()
    context = {'question_form': question_form}
    return render(request, 'myform/createform.html', context)


class IndexView(generic.ListView):
    model = Event
    template_name = 'myform/index.html'
    context_object_name = 'event_list'

    def get_queryset(self):
        event = super().get_queryset()
        return event.all()

    def get_context_data(self, **kwargs):
        event = super().get_queryset()
        context = super(IndexView, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            print(self.request.user.id)
            context['my_event'] = event.filter(owner=self.request.user.id)
        return context


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

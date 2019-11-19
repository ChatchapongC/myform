from django import forms
from django.contrib.auth.models import User
from django.forms import EmailInput, TextInput, PasswordInput, Field
from .models import Event


class UserRegistrationForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['email', 'username', 'password']
        widgets = {
            'email': EmailInput(attrs={'placeholder': 'example@email.com'}),
            'username': TextInput(attrs={'placeholder': 'username'}),
            'password': PasswordInput(attrs={'placeholder': 'password'})
        }


class EvaluateForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['event_name']
        widgets = {
            'event_name': TextInput(attrs={'placeholder': 'Event Name'})
        }

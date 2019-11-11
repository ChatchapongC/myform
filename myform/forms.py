from django import forms
from django.contrib.auth.models import User

from django.forms import EmailInput, TextInput, PasswordInput, Field


class UserRegistrationForm(forms.ModelForm):
    """
    A form that creates a user, with no privileges, from the given username and
    password.
    """

    class Meta:
        model = User
        fields = ['email', 'username', 'password']
        widgets = {
            'email': EmailInput(attrs={'placeholder': 'example@email.com'}),
            'username': TextInput(attrs={'placeholder': 'username'}),
            'password': PasswordInput(attrs={'placeholder': 'password'}),
        }

# class EvaluateForm(forms.ModelForm):
#     class Meta:
#         model = Question
#         field = ['']









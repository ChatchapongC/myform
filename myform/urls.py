from django.contrib import admin
from django.urls import path
from myform.views import HomeView, create

app_name = 'myform'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('create/', create, name='create')
]

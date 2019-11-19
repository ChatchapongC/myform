from django.contrib import admin
from django.urls import path
from myform.views import HomeView, IndexView, CreateProjectView, create_form

app_name = 'myform'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('event/', IndexView.as_view(), name='event'),
    path('project/', CreateProjectView.as_view(), name='project'),
    path('create/', create_form, name='create')
]

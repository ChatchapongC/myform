from django.contrib import admin
from django.urls import path
from myform.views import HomeView, IndexView, CreateProjectView, create_form, ContactView ,SummaryView

app_name = 'myform'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('event/', IndexView.as_view(), name='event'),
    path('project/', CreateProjectView.as_view(), name='project'),
    path('create/', create_form, name='create'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('summary/', SummaryView.as_view(), name='summary'),

]

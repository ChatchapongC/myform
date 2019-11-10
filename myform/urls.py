from django.urls import path
from myform.views import HomeView, EventListView,SignupView

app_name ='myform'

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('event/',EventListView.as_view(),name='event'),
    path('signup/',SignupView.as_view(),name='signup'),
]
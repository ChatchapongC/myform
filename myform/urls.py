from django.contrib import admin
from django.urls import path
from myform.views import HomeView, IndexView, CreateProjectView, ContactView ,SummaryView, event_delete, create_question, create_event, event_edit, \
    evaluator_view, create_question
from django.contrib.auth.decorators import login_required

app_name = 'myform'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('event/', IndexView.as_view(), name='event'),
    path('project/', CreateProjectView.as_view(), name='project'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('summary/', SummaryView.as_view(), name='summary'),
    path('create/', create_event, name='create'),
    path('create_question/<int:event_id>', create_question, name='create_question'),
    path('edit/<int:event_id>', event_edit, name='edit'),
    path('form/<int:event_id>', evaluator_view, name='evaluator'),
    path('delete/<int:event_id>', event_delete, name='delete')
]

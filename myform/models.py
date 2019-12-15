from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime



class Event(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    event_name = models.CharField(max_length=100)
    date_of_event = models.DateField(default = timezone.now)
    
    def __str__(self):
        return self.event_name

class Question(models.Model):
    event = models.ForeignKey(Event,on_delete = models.CASCADE)
    question_text = models.CharField(max_length=100)
    choice_text = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)
    choice_vote = models.IntegerField(default = 0)

    def __str__(self):
        return self.choice_text

class Evaluator(models.Model):
    responder = models.ForeignKey(User, on_delete=models.CASCADE)
    event_name = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.event_name}'
    
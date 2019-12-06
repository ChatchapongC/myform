from django.db import models
from django.utils import timezone
import datetime


class Event(models.Model):

    event_name = models.CharField(max_length=100)
    date_of_event = models.DateField(default = timezone.now)
    
    def __str__(self):
        return self.event_text

class Question(models.Model):
    event = models.ForeignKey(Event,on_delete = models.CASCADE)
    question_text = models.CharField(max_length=100)
    
    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)
    choice_vote = models.IntegerField(default = 0)

    def __str__(self):
        return self.choice_text

class Evaluator(models.Model):
    event_name = models.ForeignKey(Event, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice,  on_delete=models.CASCADE)


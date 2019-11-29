from django.db import models
from django.utils import timezone
import datetime

    
class Event(models.Model):
    name = models.CharField(max_length=100)
    date_of_event = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.event

    
class Question(models.Model):
    
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=100)
    type_of_question = models.CharField(max_length=100)


    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)

    def __str__(self):
        return self.choice_text

class Answer(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=100)

    def __str__(self):
        return self.answer_text




    

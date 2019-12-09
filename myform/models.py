from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime


class Event(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    event_name = models.CharField(max_length=100)
    event_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.event_name


class Question(models.Model):
    event = models.ForeignKey(Event, related_name='event_of_question', on_delete=models.CASCADE)
    question_text = models.CharField(max_length=100)
    choice_text = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.question_text


class Evaluation(models.Model):
    responder = models.ForeignKey(User, on_delete=models.CASCADE)
    event_name = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.event_name}'


class AnswerBase(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    response = models.ForeignKey(Evaluation, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class AnswerText(AnswerBase):
    body = models.TextField(blank=True, null=True)


class AnswerRadio(AnswerBase):
    body = models.TextField(blank=True, null=True)


class AnswerSelect(AnswerBase):
    body = models.TextField(blank=True, null=True)


class AnswerSelectMultiple(AnswerBase):
    body = models.TextField(blank=True, null=True)


class AnswerInteger(AnswerBase):
    body = models.IntegerField(blank=True, null=True)

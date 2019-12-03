from django.db import models


class Evaluator(models.Medel):
    date = models.DateTimeField(auto_now_add=True)

class Question(models.Model):
    question_text = models.CharField(max_length=100)
    
    def __str__(self):
        return self.question_textgit


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)

    def __str__(self):
        return self.choice_text

class Event(models.Model):

    event = models.CharField(max_length=100)
    
    def __str__(self):
        return self.event_text

class Answer(models.Model):

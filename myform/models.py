from django.db import models
from django.utils import timezone


class Event(models.Model):
    event = models.CharField(max_length=100)
    date_of_event = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.event

    
class Question(models.Model):

    question_text = models.CharField(max_length=100)
    type_of_question = models.CharField(max_length=100)

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    if Question.question_text == "choice":
        choice = models.CharField(max_length=100)

        def __str__(self):
            return self.choice_text

class Answer(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    if Question.question_text ==  "text":
        question = models.ForeignKey(Question, on_delete=models.CASCADE)
        answer_text = models.CharField(max_length=100)

    elif Question.question_text == "choice":
        choice = models.ForeignKey(Choice, related_name='', on_delete=models.CASCADE)
        answer_text = models.CharField(max_length=100)

    
    def __str__(self):
        return self.answer_text




    

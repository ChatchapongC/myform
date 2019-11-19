from django.contrib.auth.models import AbstractUser
from django.db import models


class Event(models.Model):
    event_name = models.CharField(max_length=30, primary_key=True)

    def __str__(self):
        return self.event_name





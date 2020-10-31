from django.contrib.auth.models import User
from django.db import models


class Notification(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=228)
    location = models.CharField(max_length=30)
    participants = models.ManyToManyField(User)
    creation_date = models.DateTimeField(auto_now_add=True)
    event_date = models.DateTimeField()
    is_finished = models.BooleanField()

from __future__ import unicode_literals
from ..login_registration.models import User
from django.db import models


class Task(models.Model):
    created_by = models.ForeignKey(User)
    date = models.CharField(max_length=10)
    time = models.TimeField()
    status = models.CharField(max_length=10, default='Pending')
    task = models.CharField(max_length=30)

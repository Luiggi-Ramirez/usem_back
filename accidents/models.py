from django.db import models
from django.utils import timezone

class Turns(models.Model):
    start = models.TimeField(default = timezone.now)
    end = models.TimeField(default = timezone.now)

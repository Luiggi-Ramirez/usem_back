from django.db import models
from django.utils import timezone

from authentication.models import CustomUser
from accidents.models import LineNumber, Turns


class DowntimeDetails(models.Model):
    user = models.ForeignKey(CustomUser, on_delete = models.DO_NOTHING)
    line_number = models.ForeignKey(LineNumber, on_delete = models.DO_NOTHING)
    start = models.TimeField()
    end = models.TimeField()
    date = models.DateField(default = timezone.now)

    def __str__(self) -> str:
        return f'{self.user} {self.line_number} {self.start} {self.end} {self.date}'
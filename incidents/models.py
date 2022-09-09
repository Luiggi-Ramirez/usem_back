from django.db import models

from authentication.models import CustomUser
from accidents.models import Turns, BusinessUnity, Area, LineNumber


class IncidentDetails(models.Model):
    '''Model for handling incidents registry'''
    user = models.ForeignKey(CustomUser, on_delete = models.DO_NOTHING)
    title = models.CharField(max_length=50)
    business_unity = models.ForeignKey(BusinessUnity, on_delete = models.DO_NOTHING)
    area = models.ForeignKey(Area, on_delete = models.DO_NOTHING)
    line_number = models.ForeignKey(LineNumber, on_delete = models.DO_NOTHING)
    turn = models.ForeignKey(Turns, on_delete = models.DO_NOTHING)
    description = models.TextField(default = "", null = True, blank = True)
    date = models.DateField(auto_now_add=True, blank=True)
    

    def __str__(self) -> str:
        return f'{self.user} {self.title} {self.business_unity} {self.area} {self.line_number} {self.turn} {self.description} {self.date}'

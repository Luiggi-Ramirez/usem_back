from django.utils import timezone
from django.db import models

from accidents.models import Area, BusinessUnity, LineNumber, Turns, CustomUser



class GenderCatalog(models.Model):
    gender = models.CharField(max_length=10)

    def __str__(self) -> str:
            return f'{self.gender}'



class Worker(models.Model):
    name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    gender = models.ForeignKey(GenderCatalog, on_delete=models.DO_NOTHING)
    
    def __str__(self) -> str:
        return f'{self.name} {self.last_name} {self.gender}'



class PeopleOnTurn(models.Model):
    user = models.ForeignKey(CustomUser, on_delete = models.DO_NOTHING)
    worker = models.ForeignKey(Worker, on_delete=models.DO_NOTHING)
    business_unity = models.ForeignKey(BusinessUnity, on_delete=models.DO_NOTHING)
    area = models.ForeignKey(Area, on_delete=models.DO_NOTHING)
    line_number = models.ForeignKey(LineNumber, on_delete=models.DO_NOTHING)
    turn = models.ForeignKey(Turns, on_delete=models.DO_NOTHING)
    date = models.DateField(default = timezone.now)

    def __str__(self) -> str:
        return f'{self.user} {self.worker}  {self.business_unity} {self.area} {self.line_number} {self.turn} {self.date}'
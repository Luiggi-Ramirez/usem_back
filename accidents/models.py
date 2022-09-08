from django.db import models
from django.utils import timezone

from authentication.models import CustomUser

class Turns(models.Model):
    start = models.TimeField(default = timezone.now)
    end = models.TimeField(default = timezone.now)
    
    
class BusinessUnity(models.Model):
    name = models.CharField(max_length=15)
    
    def __str__(self):
        return self.name
    
    
class Area(models.Model):
    business_unity = models.ForeignKey(BusinessUnity, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return f'Area: {self.name} - BU: {self.business_unity}'
    

class LineNumber(models.Model):
    area = models.ForeignKey(Area, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return f'Line Number: {self.name} - Area: {self.area}'
    
    
class AccidentType(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
    
    
class Accidents(models.Model):
    user = models.ForeignKey(CustomUser, on_delete = models.DO_NOTHING)
    business_unity = models.ForeignKey(BusinessUnity, on_delete = models.DO_NOTHING)
    area = models.ForeignKey(Area, on_delete = models.DO_NOTHING)
    line_number = models.ForeignKey(LineNumber, on_delete = models.DO_NOTHING)
    turn = models.ForeignKey(Turns, on_delete = models.DO_NOTHING)
    accident_type = models.ForeignKey(AccidentType, on_delete = models.DO_NOTHING)
    description = models.TextField(default = "", null = True, blank = True)
    date = models.DateField(default = timezone.now)
    
    def __str__(self) -> str:
        return f'{self.user} - {self.business_unity} - {self.area} - {self.line_number} - {self.turn} - {self.accident_type} - {self.description} - {self.date}'
    
    
    
    
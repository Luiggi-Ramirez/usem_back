from django.db import models

from authentication.models import CustomUser
from accidents.models import Turns, BusinessUnity, Area, LineNumber



class Production(models.Model):
    user = models.ForeignKey(CustomUser, on_delete = models.DO_NOTHING)
    business_unity = models.ForeignKey(BusinessUnity, on_delete = models.DO_NOTHING)
    area = models.ForeignKey(Area, on_delete = models.DO_NOTHING)
    line_number = models.ForeignKey(LineNumber, on_delete = models.DO_NOTHING)
    turn = models.ForeignKey(Turns, on_delete = models.DO_NOTHING)
    is_ok = models.IntegerField()
    is_bad = models.IntegerField()
    date = models.DateField(auto_now_add=True, blank=True)

    def __str__(self) -> str:
        return f'{self.user} {self.business_unity} {self.area} {self.line_number} {self.turn} {self.is_ok} {self.is_bad} {self.date}'
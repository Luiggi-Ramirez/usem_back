from django.contrib import admin
from .models import *
from accidents.models import *

# Register your models here.


admin.site.register(IncidentDetails)
admin.site.register(Turns)
admin.site.register(BusinessUnity)
admin.site.register(Area)
admin.site.register(LineNumber)


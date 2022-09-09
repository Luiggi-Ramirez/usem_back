from django.contrib import admin

from accidents.models import *

class TurnsAdmin(admin.ModelAdmin):
    list_display = ('id', 'start', 'end')
    

class BusinessUnityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class AreaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'business_unity')


class LineNumberAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'area')


class AccidentTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    

class AccidentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'business_unity', 'area', 'line_number', 'turn', 'accident_type', 'description', 'date')
    
    
admin.site.register(Turns, TurnsAdmin)
admin.site.register(BusinessUnity, BusinessUnityAdmin)
admin.site.register(Area, AreaAdmin)
admin.site.register(LineNumber, LineNumberAdmin)
admin.site.register(AccidentType, AccidentTypeAdmin)
admin.site.register(Accidents, AccidentsAdmin)
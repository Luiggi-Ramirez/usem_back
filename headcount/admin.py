from django.contrib import admin

from headcount.models import GenderCatalog, Worker, PeopleOnTurn


admin.site.register(GenderCatalog)
admin.site.register(Worker)
admin.site.register(PeopleOnTurn)

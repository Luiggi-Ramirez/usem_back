from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from authentication.models import CustomUser

class CustomUserAdmin(UserAdmin, admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "email", "phone_number", "date_joined")


admin.site.register(CustomUser, CustomUserAdmin)

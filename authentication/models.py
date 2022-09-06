from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    username = models.CharField(max_length=50, unique=False, null=True, blank=True)
    email = models.EmailField(max_length=40, unique=True)
    phone_number = models.CharField(max_length=13, unique=False, null=True, blank=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password']
    
    def __str__(self):
        return f"{self.id} {self.first_name} {self.last_name} {self.email} {self.phone_number}"
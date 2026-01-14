from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, default='')
    country_code = models.CharField(max_length=5, blank=True, default='+31')
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=20, blank=True, default='')
    nationality = models.CharField(max_length=50, blank=True, default='')
    
    # New Address Fields
    street_address = models.CharField(max_length=255, blank=True, default='')
    city = models.CharField(max_length=100, blank=True, default='')
    postal_code = models.CharField(max_length=20, blank=True, default='')
    
    def __str__(self):
        return self.username
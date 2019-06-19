from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    api_key = models.CharField(max_length=100, null=True, blank=True )
    api_token = models.CharField(max_length=100, null=True, blank=True)

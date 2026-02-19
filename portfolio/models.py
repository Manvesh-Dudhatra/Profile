from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    mobile = models.CharField(blank=True)

class Inquiry(models.Model):
    name = models.CharField(max_length= 30)
    cname = models.CharField(max_length= 50)
    address = models.TextField(null = False, blank=False)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    message = models.TextField(null = False, blank=False)


from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.html import escape, mark_safe

class User(AbstractUser):
    is_patient = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    

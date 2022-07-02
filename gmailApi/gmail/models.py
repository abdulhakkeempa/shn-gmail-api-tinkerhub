from statistics import mode
from django.db import models

# Create your models here.

class email(models.Model):
    email = models.CharField(max_length=100,null=False,blank=False)

class OTP(models.Model):
    otp = models.CharField(max_length=10,null=False,blank=False)
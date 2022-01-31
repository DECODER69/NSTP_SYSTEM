from django.db import models
from datetime import datetime
from django.utils import timezone

now = timezone.now

# Create your models here.
class registration(models.Model):
    idnum = models.CharField(max_length=12, primary_key=True)
    lname = models.CharField(max_length=20, null=False)
    fname = models.CharField(max_length=30, null=False)
    minitial = models.CharField(max_length=1, null=True)
    address = models.CharField(max_length=100)
    cpnumber = models.DecimalField(max_digits=11, decimal_places=0)
    email = models.EmailField(null=False)
    gender = models.CharField(max_length=6, null=False)
    age = models.DecimalField(max_digits=3, decimal_places=0, null=False)
    bdate = models.CharField(max_length=15, null=False)
    password = models.CharField(max_length=20, null=False)
    section = models.CharField(max_length=20, null=False)
    
    
    def __str__(self):
        return self.idnum
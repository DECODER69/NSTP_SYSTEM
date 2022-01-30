from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


# class CustomUser(AbstractUser):
    
    
    


# Create your models here.
class registration(models.Model):
    field_rotc = 0
    field_cwts = 1
    field_choices = [(field_rotc, 'ROTC'), (field_cwts, 'CWTS')]
    idnum = models.CharField(max_length=12, primary_key=True)
    lname = models.CharField(max_length=20, default='')
    fname = models.CharField(max_length=30, default='')
    minitial = models.CharField(max_length=1, default='')
    address = models.CharField(max_length=100, default='')
    cpnumber = models.DecimalField(max_digits=11, decimal_places=0, default='')
    email = models.EmailField(max_length=254, null=True)
    gender = models.CharField(max_length=6, default='')
    age = models.DecimalField(max_digits=3, decimal_places=0)
    bdate = models.CharField(max_length=15, default='')
    password = models.CharField(max_length=20, default='')
    section = models.CharField(max_length=20, default='')
    field = models.CharField(max_length=20, default='')
    
    def __str__(self):
        return self.idnum
    

    
class certifications(models.Model):
    STATUS = (
        ("Pending", "PENDING" ),
        ("Approved", "APPROVED"),
        )
    cert_email = models.EmailField(max_length=254, null=True)
    cert_fullname = models.CharField(max_length=100)
    cert_course = models.CharField(max_length=20 )
    cert_datereq = models.CharField(max_length=20 )
    cert_document = models.CharField(max_length=20 )
    cert_status = models.CharField(max_length=20, choices=STATUS, default='PENDING')
    
    def __str__(self):
        return self.cert_email
    
    
from django.db import models

# Create your models here.
<<<<<<< HEAD
class registration(models.Model):
    idnum = models.CharField(max_length=12, primary_key=True)
    lname = models.CharField(max_length=30)
    fname = models.CharField(max_length=30)
    minitial = models.CharField(max_length=1)
    address = models.CharField(max_length=100)
    cpnumber = models.DecimalField(max_digits=11, decimal_places=0)
    email = models.EmailField()
    gender = models.CharField(max_length=6)
    age = models.DecimalField(max_digits=3, decimal_places=0)
    bdate = models.CharField(max_length=15)
    password = models.CharField(max_length=20)
    
    
    
class StudentsInformation(models.Model):  
    studentID = models.CharField(max_length=20)  
    studentName = models.CharField(max_length=100)  
    studentEmail = models.EmailField()  
    studentcontact = models.CharField(max_length=15)
    
    
class admin(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
=======
>>>>>>> db7afe168e6d0af4020469237ef6ab17cf4df33e

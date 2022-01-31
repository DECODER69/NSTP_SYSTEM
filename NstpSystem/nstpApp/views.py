from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from pyexpat.errors import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import context
from .models import registration
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required, permission_required
import mysql.connector as sql

# Create your views here.



def index(request):
    return render(request, 'html/index.html')
def navbar(request):
    return render(request, 'base.html')

def login(request):
    return render(request, 'templates/html/login.html')
def register(request):
    return render(request, 'html/signup.html')

def rotclist(request):
    return render(request, 'html/rotclist.html')
def cwtslist(request):
    return render(request, 'html/cwtslist.html')
def dashboard(request):
    return render(request, 'html/Dashboard.html')
def platoon(request):
    return render(request, 'html/Platoon.html')
def cwts(request):
    return render(request, 'html/Cwts.html')
def certification(request):
    return render(request, 'html/Certification.html')




def registerprocess(request):
    if request.method == 'POST':
        idnumber = request.POST.get('idnum')
        lname = request.POST.get('surename')
        fname = request.POST.get('firstname')
        minitial = request.POST.get('middle')
        address = request.POST.get('address')
        cpnumber = request.POST.get('contact')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        bdate = request.POST.get('birthday')
        password = request.POST.get('password')
        
        
        try:
            n = registration.objects.get(idnum=idnumber)
            return render(request, 'html/signup.html', {'error_message': 'ID Number already exists: ' + idnumber})
        
        except ObjectDoesNotExist:
            user = registration.objects.create(idnum=idnumber, lname=lname, fname=fname, minitial=minitial, address=address, cpnumber=cpnumber, email=email, gender=gender,
                                               age=age, bdate=bdate, password=password)
            user.save()
            return HttpResponseRedirect('/register')
        
def userlogin(request):
    if request.method=="POST":
        m=sql.connect(host="localhost",user="admin",password="",database='nstpsystem')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="username":
                idnum=value
            if key=="password":
                password=value
        
        c="select * from nstpapp_registration where idnum='{}' and password='{}'".format(idnum,password)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            return render(request,'html/login.html')
            
        else:
            return render(request, 'html/Dashboard.html')

    return render(request, 'html/login.html')



from os import name
from pyexpat.errors import messages
from django.contrib import messages 
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import context
from .models import registration
from .models import certifications

from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required, permission_required
import mysql.connector as sql
from django.contrib.auth.models import User, auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

idnum=''
password=''






def index(request):
    return render(request, 'activities/index.html')
def login(request):
    return render(request, 'activities/login.html')
def register(request):
    return render(request, 'activities/signup.html')

def navbar(request):
    data = registration.objects.all()
    return render(request, 'activities/base.html', {'data': data})
def rotclist(request):
    list = registration.objects.filter(field='ROTC')
    return render(request, 'activities/rotclist.html', {'list': list})
def cwtslist(request):
    list1 = registration.objects.filter(field='CWTS')
    return render(request, 'activities/cwtslist.html', {'list1': list1})
def dashboard(request):
    return render(request, 'activities/Dashboard.html')
def requested(request):
    requests = certifications.objects.all()
    return render(request, 'activities/certification.html', {'requests': requests})
def platoon(request):
    return render(request, 'activities/Platoon.html')
def cwts(request):
    return render(request, 'activities/Cwts.html')
def certification(request):
    return render(request, 'activities/Certification.html')

def userlogout(request):
	return render(request, 'activities/login.html')

def certification(request):
    requests = certifications.objects.all()
    return render(request, 'activities/certification.html', {'requests': requests})

def admincertificate(request):
    request1 = certifications.objects.all()
    return render(request, 'activities/admincertification.html', {'request1': request1})

def navadmin(request):
    return render(request, 'activities/NavAdmin.html')






    

def registerprocess(request):
    if request.method == 'POST':
        last_name = request.POST['last_name']
        first_name = request.POST['first_name']
        email = request.POST['email']
        password = request.POST['password']
        username=request.POST['username']
        
        user = User.objects.create(last_name=last_name, first_name=first_name, email=email, password=password, username=username)
        user.save()
        return render(request, 'activities/login.html')
    else:
        return render(request, 'activities/signup.html')
        
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
            return render(request, 'activities/login.html')
            
        else:
            name = registration.objects.filter(idnum=idnum)
            return render(request, 'activities/Dashboard.html', {'name': name})

    return render(request, 'activities/login.html')

# def userlogin(request):
#     if request.method == "POST":
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return render(request, 'activities/Dashboard.html')
#         else:
#             return render(request, 'activities/login.html')
       
#     else:
#         return render(request, 'activities/Dashboard.html')
            


def cert(request):
    if request.method == 'POST':
        cert_email = request.POST.get('cert_email')
        cert_fullname = request.POST.get('cert_fullname')
        cert_course = request.POST.get('cert_course')
        cert_datereq = request.POST.get('cert_datereq')
        cert_document = request.POST.get('cert_document')
        certificate = certifications.objects.create(cert_email=cert_email, cert_fullname=cert_fullname, cert_course=cert_course, cert_datereq=cert_datereq, cert_document=cert_document)
        certificate.save()
        return redirect('/certification')
       
        
       
def logout_user(request):
    logout(request)
    messages.success(request, ("You were Log out, please Log in again"))
    return redirect('/')



# def updatestatus(request, cert_email):
#     data = certifications.objects.get(id=cert_email)
#     form = request.POST(instance=data)
#     if request.method == "POST":
#         form = AdminUpdate(request.POST, instance=data)
#         if form.is_valid():
#             form.save()
#             return redirect('/admin/')
#     # content = {'datas':datas, 'form':form}
#     content = {'form':form}
#     return render(request, 'admins/form_modification.html', content)

        
        
# def delete(request, cert_email):
#     data = certifications.objects.get(id=cert_email)
#     data.delete()
#     return redirect('/admincertificate')    
def delete(request, id):
    member = certifications.objects.get(id=id)
    member.delete()
    return redirect('/admincertificate')

    



def update(request, id):
    if request.method == 'POST':
        data = certifications.objects.get(id=id)
        data.cert_status = request.POST['status']
        data.save()
        return redirect('/admincertificate')
    else:   
        return redirect('/admincertificate')
        
            
    







  
            
    


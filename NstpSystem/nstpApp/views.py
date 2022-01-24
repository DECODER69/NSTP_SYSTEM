from django.shortcuts import render
from django.http import HttpResponse
<<<<<<< HEAD
from .models import StudentsInformation  
=======
>>>>>>> db7afe168e6d0af4020469237ef6ab17cf4df33e



# Create your views here.


def index(request):
    return render(request, 'activities/index.html')

def login(request):
    return render(request, 'activities/login.html')


def studentCreate(request):
    students = StudentsInformation.objects.create(
	s_id = request.GET['studentID'],
	s_name = request.GET['studentName'],
	s_email = request.GET['studentEmail'],
	s_contact = request.GET['studentContact'],
	)
    return render(request,'activities/create.html')


def read(request):  

    students = StudentsInformation.objects.all() 
    context ={'students':students}
    return render(request,"activities/read.html", context) 

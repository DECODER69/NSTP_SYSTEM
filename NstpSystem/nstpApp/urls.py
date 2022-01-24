from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('studentCreatee/', views.studentCreate, name='studentCreate'),  
    path('read/',views.read, name='read'), 
   
]

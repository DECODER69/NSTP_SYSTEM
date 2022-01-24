from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
<<<<<<< HEAD
    path('studentCreatee/', views.studentCreate, name='studentCreate'),  
    path('read/',views.read, name='read'), 
=======
>>>>>>> db7afe168e6d0af4020469237ef6ab17cf4df33e
   
]

from django.urls import path
from . import views
from django.conf.urls import static
from django.conf import settings


app_name = 'activities'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('registerprocess/', views.registerprocess, name='registerprocess'),
    path('userlogin/', views.userlogin, name='userlogin'),
    path('navbar/', views.navbar, name='navbar'),
    path('rotclist/', views.rotclist, name='rotclist'),
    path('cwtslist/', views.cwtslist, name='cwtslist'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('platoon/', views.platoon, name='platoon'),
    path('cwts/', views.cwts, name='cwts'),
    path('certification/', views.certification, name='certification'),

   
]

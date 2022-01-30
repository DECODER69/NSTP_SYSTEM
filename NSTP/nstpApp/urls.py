from django.urls import path
from . import views
from django.conf.urls import static
from django.conf import settings
from django.urls import include, path
from django.contrib import admin

from django.urls import include, re_path


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
    path('userlogout/', views.userlogout, name='userlogout'),
    path('certification/', views.certification, name='certification'),
    path('cert/', views.cert, name='cert'),
    path('requested/', views.requested, name='requested'),
    path('admincertificate/', views.admincertificate, name='admincertificate'),
    path('navadmin', views.navadmin, name='navadmin'),
    path('logout_user', views.logout_user, name='logout_user'),
    path('delete/<str:id>', views.delete, name='delete'),
    path('update/', views.update, name='update'),
    # re_path(r'^delete/', views.delete, name='delete'),
    # path('updatestatus', views.updatestatus, name='updatestatus'),

   
]

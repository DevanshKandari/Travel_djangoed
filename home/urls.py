from django.contrib import admin
from django.urls import path , include
from home import views

urlpatterns = [
    path ('', views.index, name='home'),
    path ('index', views.index, name='home'),
    path ('about', views.about , name='about'),
    path ('form', views.form , name='form'),
    path ('signin' , views.signin , name='signin'),
    path ('signout' , views.signout , name='signout'),
    path ('blog' , views.blogg , name='blog'),
    path ('delete/<id>/' , views.delete_b , name='delete_b'),
    
    
]

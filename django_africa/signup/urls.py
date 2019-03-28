# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all', views.all, name='all'),
    path('new', views.signup_new, name="signup_new")
]
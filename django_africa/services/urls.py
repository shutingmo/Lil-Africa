from django.urls import path
from . import views

urlpatterns = [
    path('', views.services, name = 'services'),
    path('all', views.all, name = 'all'),
    path('new', views.services_appt_new, name="services_appt_new")
]
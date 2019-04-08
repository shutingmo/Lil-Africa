from django.shortcuts import render
from django.http import HttpResponse
from .models import Service_Appt
# from .forms import Post_Service_Appt
from .forms import CustomUserCreationForm
from django.shortcuts import redirect
from django_africa.generic import BSModalCreateView
from django.urls import reverse_lazy
from django_africa import templates
from django_africa import views

# Create your views here.
def services(request):
    return render(request, 'services/servicesInfo.html')

# shows all services sign up forms completed
def all(request):
    services = Service_Appt.objects.order_by('name')
    return render(request, 'services/servicesApptAll.html', {'services' : services})

class servicesView(BSModalCreateView):
    form_class = CustomUserCreationForm
    # template_name='django_africa/servicesNew.html'
    template_name='services/serviceNew.html'

    success_message = 'Success: Sign up'
    success_url = reverse_lazy(views.homepage)
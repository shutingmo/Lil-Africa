from django.shortcuts import render
from django.http import HttpResponse
from services.models import Service_Appt
from signup.models import Signup_Form
from services.forms import CustomUserCreationForm
from signup.forms import Post_Signup_Form
from django.shortcuts import redirect
from django.views import generic
from .generic import BSModalCreateView
from django.urls import reverse_lazy

def _form_view(request, template_name='django_africa/homepage.html', form_class=Post_Signup_Form, model_class=Signup_Form):
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            model_class = form.save(commit=False)
            model_class.save()
            return redirect('homepage')
    else:
        form = form_class()
    return render(request, template_name, {'form' : form})

def homepage(request):
    # return render(request, 'django_africa/homePage.html')
    return _form_view(request)


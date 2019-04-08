from django import forms
from .models import Service_Appt
from django_africa.forms import BSModalForm
from django_africa.mixins import PopRequestMixin, CreateUpdateAjaxMixin

class CustomUserCreationForm(BSModalForm):
    class Meta:
        model = Service_Appt
        # model = User
        fields = ("name", "email", "number")

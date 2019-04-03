from django import forms
from .models import Service_Appt
from django_africa.forms import BSModalForm
from django_africa.mixins import PopRequestMixin, CreateUpdateAjaxMixin
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
# class Post_Service_Appt(forms.ModelForm):
#     class Meta:
#         model = Service_Appt
#         fields = ("name", "email", "number")


# class CustomUserCreationForm(PopRequestMixin, CreateUpdateAjaxMixin):
#     class Meta:
#         model = Service_Appt
#         # model = User
#         fields = ("name", "email", "number")

# class Post_Service_Appt(BSModalForm):
#     class Meta:
#         model = Service_Appt
#         fields = ("name", "email", "number")


class CustomUserCreationForm(BSModalForm):
    class Meta:
        model = Service_Appt
        # model = User
        fields = ("name", "email", "number")

from django import forms
from .models import Service_Appt

class Post_Service_Appt(forms.ModelForm):
    class Meta:
        model = Service_Appt
        fields = ("name", "email", "number")
from django import forms
from .models import Signup_Form

class PostSignupForm(forms.ModelForm):
    class Meta:
        model = Signup_Form
        fields = ("name", "email", "number")
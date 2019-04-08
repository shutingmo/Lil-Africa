from django import forms
from .models import Signup_Form

class Post_Signup_Form(forms.ModelForm):
    criminal = forms.BooleanField(required=False)
    resume = forms.FileField(required=False)

    class Meta:
        model = Signup_Form
        fields = ("name", "email", "number", "role", "dob", "last_employment", 'criminal', 'resume')
from django import forms
from .models import Signup_Form

class PostSignupForm(forms.ModelForm):
    criminal = forms.BooleanField(required=False)
    class Meta:
        model = Signup_Form
        fields = ("name", "email", "number", "role", "dob", "last_employment", 'criminal', 'resume')
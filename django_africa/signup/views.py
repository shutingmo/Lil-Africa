from django.shortcuts import render
from django.http import HttpResponse
from .models import Signup_Form
from .forms import PostSignupForm
from django.shortcuts import redirect

# Create your views here.
def index(request):
    # return HttpResponse("You are on the sign in index")
    # signups = Signup_Form.objects.order_by('name')
    return render(request, 'signup/homePage.html')

def all(request):
    signups = Signup_Form.objects.order_by('name')
    return render(request, 'signup/signupAll.html', {'signups' : signups})

def signup_new(request):
    if request.method == "POST":
        form = PostSignupForm(request.POST)
        if form.is_valid():
            Signup_Form = form.save(commit=False)
            # Signup_Form.name = request.user.name
            # Signup_Form.email = request.user.email
            # Signup_Form.number = request.user.number
            # Signup_Form.name = request.user
            Signup_Form.save()
            return redirect('all')
    else:
        form = PostSignupForm()
    
    
    # return render(request, 'signup/signupNew.html', {'form' : form})
    return render(request, 'signup/signupNew.html', {'form' : form})




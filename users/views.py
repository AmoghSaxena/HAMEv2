from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from .forms import UserCreationForm, LoginForm
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.conf import settings

subject = 'Test Email'
message = 'This is a test email sent using SMTP in Django.'
from_email = settings.EMAIL_HOST_USER
recipient_list = ['rexter.digivalet@gmail.com']
print(settings.EMAIL_HOST_USER)
# send_mail(subject, message, from_email, recipient_list)

# Create your views here.
# Home page
def index(request):
    return render(request, 'index.html')

# signup page
def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


# function to check if the input is a valid email address also checks if the email is already registered also email should be non spam email, eg: gmail, outlook, live, etc should be valid
def is_valid_email(email):
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return True
    return False

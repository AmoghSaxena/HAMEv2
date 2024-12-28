# This is class based view for user creation in django
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.contrib.auth.models import User
from django.contrib import messages
from users.models import TempUser, Profile
from newsletter.models import Subscribers
from .ValidEmailCheck import IPQS
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
import random


context = {}
class UserCreation(View):
    def get(self, request):
        context['message'] = ""
        usernames_list = User.objects.values_list('username', flat=True)
        context['usernames_list'] = usernames_list
        return render(request, 'signup.html', context)
    
    def post(self, request):
        if 'otp_btn' in request.POST:
            otp = request.POST.get('otp')
            username = request.POST.get('username')
            context['username'] = username
            a = get_object_or_404(TempUser, username=username)
            if a.otp == int(otp):
                # User Creation in Profile Model
                user = User.objects.create_user(username=a.username, password=a.password, email=a.email, first_name=a.first_name, last_name=a.last_name)
                Profile.objects.create(user=user)
                TempUser.objects.filter(username=username).delete()
                Subscribers.objects.create(email=a.email)
                messages.success(request, 'User created successfully')
                return redirect('login')

                # User.objects.create_user(username=a.username, password=a.password, email=a.email)
                # TempUser.objects.filter(username=username).delete()
                # Subscribers.objects.create(email=a.email)
                # messages.success(request, 'User created successfully')
                # return redirect('login')
            else:
                messages.error(request, 'Invalid OTP')
                return render(request, 'submitotp.html', context)

        elif 'register' in request.POST:
            username = request.POST.get('username')
            context['username'] = username
            password = request.POST.get('password')
            email = request.POST.get('email')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            try:
                get_object_or_404(User, username=username)
                messages.error(request, 'Username already exists')
                return render(request, 'signup.html', context)
            except:
                otp = random.randint(1000, 9999)
                subject = 'OTP Verification'
                message = f'Your OTP is {otp}'
                from_email = settings.EMAIL_HOST_USER
                recipient_list = [email]
                try:
                    ipqs = IPQS()
                    valid, comment = ipqs.emailvalidator_address(email)
                    if not valid:
                        messages.error(request, comment)
                        return render(request, 'signup.html', context)
                    additional_params = {
                        'timeout' : 7,
                        'fast' : 'false',
                        'abuse_strictness' : 0
                        }
                    valid, comment = ipqs.email_validation_api(email, additional_params)
                    if not valid:
                        messages.error(request, comment)
                        return render(request, 'signup.html', context)
                    send_mail(subject, message, from_email, recipient_list)
                    print(otp)
                    TempUser.objects.create(username=username, password=password, email=email, otp=otp, first_name=first_name, last_name=last_name)
                    return render(request, 'submitotp.html', context)
                except ConnectionRefusedError:
                    messages.error(request, 'Unable to send Email. Please try again later')
                    return render(request, 'signup.html', context)
                except:
                    messages.error(request, 'Invalid Email Address')
                    return render(request, 'signup.html', context)
                
        
    
class UserLogin(View):
    def get(self, request):
        return render(request, 'login.html')
    
    def post(self, request):
        if 'logout' in request.POST:
            logout(request)
            return redirect('login')
        
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Logged in successfully')    
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
        return render(request, 'login.html')
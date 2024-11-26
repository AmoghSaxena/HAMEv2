from django.shortcuts import render, redirect
from .models import Subscribers
from django.contrib import messages

def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('EMAIL')
        next_url = request.POST.get('next', '/')
        if Subscribers.objects.filter(email=email).exists():
            messages.warning(request, 'You are already subscribed to our newsletter.')
            return redirect(next_url)
        else:
            Subscribers.objects.create(email=email)
            messages.success(request, 'You have successfully subscribed to our newsletter.')
            return redirect(next_url)
    else:
        redirect ('login')

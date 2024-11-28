from django.shortcuts import render
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')

def listing(request):
    return render(request, 'index.html')

def property(request, id):
    messages.success(request, f'{id}')
    return render(request, 'properties.html')
from django.shortcuts import render
from .models import Profile

def home(request):
    profile = Profile.objects.first()
    return render(request, 'pages/home.html', {'profile': profile})

def about(request):
    profile = Profile.objects.first()
    return render(request, 'pages/about.html', {'profile': profile})

def contact(request):
    profile = Profile.objects.first()
    return render(request, 'pages/contact.html', {'profile': profile})

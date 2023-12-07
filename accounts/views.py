from django.shortcuts import render
from .models import UserProfile
from django.shortcuts import get_object_or_404
# Create your views here.

def add_education(request):
    return render(request,'accounts/add-education.html',context={})

def add_experience(request):
    return render(request,'accounts/add-experience.html',context={})

def create_profile(request):
    return render(request,'accounts/create-profile.html',context={})

def dashboard(request):
    return render(request,'accounts/dashboard.html',context={})

def login(request):
    return render(request,'accounts/login.html',context={})

def profile(request,slug):
    user_profile = get_object_or_404(UserProfile,slug=slug)
    # user_profile = UserProfile.objects.get(id=id)
    return render(request,'accounts/profile.html',
                  context={"user_profile":user_profile})

def profiles(request):
    user_profiles = UserProfile.objects.all()
    return render(request,'accounts/profiles.html',
                  context={"user_profiles":user_profiles})

def register(request):
    return render(request,'accounts/register.html',context={})

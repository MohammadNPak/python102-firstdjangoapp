from django.shortcuts import render
from .models import UserProfile
from django.http import HttpResponse

# Create your views here.
def addeducation (request):
    if request.method == "GET":
        return render(request,'accounts/add-education.html',{})

def addexperience (request):
    if request.method == "GET":
        return render(request,'accounts/add-experience.html',{})
def createprofile (request):
    if request.method == "GET":
        return render(request,'accounts/create-profile.html',{})
def dashboard (request):
    if request.method == "GET":
        return render(request,'accounts/dashboard.html',{})
def login (request):
    if request.method == "GET":
        return render(request,'accounts/login.html',{})
def profile (request):
    if request.method == "GET":
        return render(request,'accounts/profile.html',{})
def profiles (request):
    all_profiles = UserProfile.objects.all()
    if request.method == "GET":
        return render(request,'accounts/profiles.html',context={"all_profiles":all_profiles})
def register (request):
    if request.method == "GET":
        return render(request,'accounts/register.html',{})
from django.shortcuts import render,redirect
from django.urls import reverse,reverse_lazy
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.views import View
from django.views.generic import ListView,DetailView,CreateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import (
    authenticate,
    login as django_login,
    logout as django_logout)

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import UserProfile,Experience
from .forms import UserProfileCreationForm

# Create your views here.

def add_education(request):
    return render(request,'accounts/add-education.html',context={})

def add_experience(request):
    return render(request,'accounts/add-experience.html',context={})

def create_profile(request):
    return render(request,'accounts/create-profile.html',context={})

@login_required
def dashboard(request):
    return render(request,'accounts/dashboard.html',context={})

def login(request):
    if request.method =="GET":
        form = AuthenticationForm()
    elif request.method =="POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username= form.cleaned_data["username"]
            password= form.cleaned_data["password"]
            user = authenticate(request,username=username,password=password)
            if user is not None:
                django_login(request,user)
                messages.add_message(request,messages.SUCCESS,f"welcome {username}!")
                return redirect(reverse("dashboard"))
            messages.add_message(request,messages.ERROR,f"user {username} was not found!")
    return render(request,'accounts/login.html',context={"form":form})
    
def logout(request):
    django_logout(request)
    return redirect(reverse("index"))


class UserProfileUpdateView(View,LoginRequiredMixin):

    def get(self,request,slug):
        user_profile = request.user.userprofile
        form = UserProfileCreationForm(instance=user_profile)
        return render(request,"accounts/create-profile.html",{"form":form})

    def post(self,request,slug):
        form = UserProfileCreationForm(
            data=request.POST,
            files=request.FILES,
            instance=request.user.userprofile
            )

        if form.is_valid():
            form.save()
            return redirect(reverse("dashboard"))
        return render(request,"accounts/create-profile.html",{"form":form})


# def profiles(request):
#     user_profiles = UserProfile.objects.all()
#     return render(request,'accounts/profiles.html',
#                   context={"user_profiles":user_profiles})


# def profile(request,slug):
#     user_profile = get_object_or_404(UserProfile,slug=slug)
#     # user_profile = UserProfile.objects.get(id=id)
    
#     return render(request,'accounts/profile.html',
#                   context={"user_profile":user_profile})

class ProfileDetailView(DetailView):
    model=UserProfile
    slug_url_kwarg="slug"
    # template_name="accounts/userprofile.html"


class ProfileListView(ListView):
    model = UserProfile

    # template_name = "accounts/profiles.html"
    # queryset = UserProfile.objects.all()
    # context_object_name = "profiles"


class ExperienceCreateView(CreateView,LoginRequiredMixin):
    model=Experience
    success_url=reverse_lazy("index")
    fields = ["company","start_date",
              "end_date","position",
              "description",]
    
    def form_valid(self, form):
        form.instance.userprofile = self.request.user.userprofile
        form.save()
        return super().form_valid(form)
    
    







    




def register(request):
    if request.method=="GET":
        form = UserCreationForm()
        return render(request,
                      'accounts/register.html',
                      context={"form":form})
    
    elif request.method=="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password1 = form.cleaned_data["password1"]
            password2 = form.cleaned_data["password2"]
            # email = form.cleaned_data["email"]
            User.objects.create_user(
                username=username,
                password=password1
                # email=email
                )
            messages.add_message(request,messages.SUCCESS,f"user {username} was created successfully!")
            return redirect(reverse('login'))

        else:
            return render(request,
                      'accounts/register.html',
                      context={"form":form})
        
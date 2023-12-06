from django.urls import path
from .views import addeducation, addexperience, createprofile, dashboard, login, profile, profiles, register

urlpatterns = [
    path('add-education', addeducation, name='addeducation'),
    path('add-experience', addexperience, name='addexperience'),
    path('create-profile', createprofile, name='createprofile'),
    path('dashboard', dashboard, name='dashboard'),
    path('login', login, name='login'),
    path('profile', profile, name='profile'),
    path('profiles', profiles, name='profiles'),
    path('register', register, name='register')
]

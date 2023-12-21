from django.urls import path
from . import views

urlpatterns = [
        path("add-education",views.add_education,name="add-education"),
        
        path("add-experience",
             views.ExperienceCreateView.as_view(),
             name="add-experience"),
             
        path("create-profile",views.create_profile,name="create-profile"),
        path("dashboard",views.dashboard,name="dashboard"),
        path("login/",views.login,name="login"),
        path("logout/",views.logout,name="logout"),
        
        path("profile/<slug:slug>/update",
             views.UserProfileUpdateView.as_view(),
             name="profile_detail"),
        
        path("profile/<slug:slug>",
             views.ProfileDetailView.as_view(),
             name="profile_detail"),

        # path("profiles",views.profiles,name="profiles"),
        path("profiles",views.ProfileListView.as_view(),name="profiles"),
        path("register",views.register,name="register"),
]
    
from django.db import models
from django.urls import reverse
# Create your models here.
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    job_title = models.CharField(max_length=200,null=True,blank=True)
    slug = models.SlugField(unique=True,null=True,blank=True)
    bio = models.TextField(null=True)
    picture = models.ImageField(upload_to="profiles_picture",null=True)

    def __str__(self) -> str:
        return f"UserProfile({self.user.first_name} {self.user.last_name})"
    
    def get_full_name(self):
        return self.first_name+" "+ self.last_name
    
    def get_absolute_url(self):
        return reverse("profile_detail", kwargs={"slug": self.slug})


class Experience(models.Model):
    userprofile = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    company = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date=models.DateField(null=True)
    position = models.CharField(max_length=200)
    description=models.TextField()

    def __str__(self) -> str:
        return f"Experience(user={self.userprofile.user.username})"


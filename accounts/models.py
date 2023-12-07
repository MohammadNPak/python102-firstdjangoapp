from django.db import models
from django.urls import reverse
# Create your models here.

class UserProfile(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    job_title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    def __str__(self) -> str:
        return f"UserProfile({self.first_name} {self.last_name})"
    
    def get_full_name(self):
        return self.first_name+" "+ self.last_name
    
    def get_absolute_url(self):
        return reverse("profile_detail", kwargs={"slug": self.slug})
    
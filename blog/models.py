from collections.abc import Iterable
from django.db import models
from accounts.models import UserProfile
from django.utils.text import slugify
from django.urls import reverse
# Create your models here.


class Post(models.Model):
    slug = models.SlugField(null=False,unique=True,blank=True)
    body = models.TextField()
    title = models.CharField(max_length=200,null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        related_name="posts")


    def __str__(self) -> str:
        return f"Post({self.body[:30]}...)"

    def save(self,*args,**kwargs):
        if not self.slug :
            self.slug = f"{slugify(self.title)}"
        return super().save(*args,**kwargs)
    
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.slug})
    
    

class Comment(models.Model):
    body = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    author = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE)

    def __str__(self):
        return f"Comment('{self.body[:20]}...')"
    


class Test(models.Model):
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='testimage')


from django.db import models

# Create your models here.

class UserProfile(models.Model):
    name = models.CharField(max_length=100,null=False)
    last_name = models.CharField(max_length=100,null=False)
    job_titel = models.CharField(max_length=100,null=False)
    company = models.CharField(max_length=100,null=False)
    city = models.CharField(max_length=100,null=False)

    def __str__(self) -> str:
        return f"Account({self.name}, {self.last_name}...)"



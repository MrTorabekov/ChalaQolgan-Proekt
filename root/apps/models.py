from django.db import models
from django.contrib.auth.models import AbstractUser

class Products(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField(upload_to='images')



class Users(AbstractUser):
    staff = models.CharField(max_length=40,blank=True,null=True)



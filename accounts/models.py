from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone = models.CharField(max_length=10 , blank=True , null=True)
    address = models.CharField(max_length=250 , blank=True , null=True)
    image = models.ImageField(upload_to='photos/%y/%m/%d' , blank=True , null=True)


    def __str__(self):
        return self.username
# Create your models here.

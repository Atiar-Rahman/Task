from django.db import models
from django.contrib.auth.models import AbstractUser
from users.managers import CustomUser
# Create your models here.

class User(AbstractUser):
    username=None #remove username
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    address = models.TextField(blank=True,null=True)
    phone_number = models.CharField(max_length=15,blank=True,null=True)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]

    objects = CustomUser()

    def __str__(self):
        return self.email
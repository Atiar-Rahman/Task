from django.db import models

# Create your models here.

class Student(models.Model):
    GENDER_CHOICES = (
        ('male','Male'),
        ('female','Female'),
        ('others','Others'),
    )
    name = models.CharField(max_length=100)
    fathers_name = models.CharField(max_length=100)
    mothers_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    present_address = models.TextField()
    parmanent_address = models.TextField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10,choices=GENDER_CHOICES,default='male')
    dob = models.DateField()
    description = models.TextField()
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    
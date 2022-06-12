from pyexpat import model
from django.db import models

# Create your models here.
class RegistrationModel(models.Model):
    fname=models.CharField(max_length=75)
    lname=models.CharField(max_length=75)
    email=models.EmailField()
    mobile=models.CharField(max_length=11)
    website=models.CharField(max_length=75)
    password=models.CharField(max_length=255)
    confirm=models.CharField(max_length=255)
    image=models.ImageField(upload_to='media')
    date=models.DateField(auto_now=True)

class AdminModel(models.Model):
    name=models.CharField(max_length=255)
    password=models.CharField(max_length=50)

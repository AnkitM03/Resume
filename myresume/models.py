from django.db import models

# Create your models here.

class Resume(models.Model):
    First_Name=models.CharField(max_length=30)
    Last_Name=models.CharField(max_length=30)
    Age =models.CharField(max_length=30)
    Nationality=models.CharField(max_length=30)
    Freelance=models.CharField(max_length=30, default="Available")
    Address=models.CharField(max_length=30)
    Phone=models.CharField(max_length=10)
    Email=models.CharField(max_length=30)
    Langages=models.CharField(max_length=50)
    Hobby=models.CharField(max_length=30)


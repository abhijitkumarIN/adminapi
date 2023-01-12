from django.db import models

# Create your models here.


# employee model

class Company(models.Model):
    name = models.CharField(max_length=60)
    detail = models.CharField(max_length=300)
    location = models.CharField(max_length=70)
    about = models.TextField()
    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)


class Employee(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=60,null=True)
    email = models.EmailField(max_length=60, unique=True, null=True)
    job_type = models.CharField(max_length=50, null=True)
    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)


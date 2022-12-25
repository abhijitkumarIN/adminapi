from django.db import models

# Create your models here.


# employee model

class Employee(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField(max_length=60, unique=True)
    job_type = models.CharField(max_length=50)
    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    created = models.DateTimeField()


class Company(models.Model):
    Emplyees = models.ForeignKey(Employee, on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    detail = models.CharField(max_length=300)
    location = models.CharField(max_length=70)
    about = models.TextField()
    created = models.DateTimeField()
    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

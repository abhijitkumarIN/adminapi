from django.db import models

# Create your models here.
class Collage(models.Model):
    name= models.CharField(max_length=60)
    location= models.TextField(max_length=180)
    created_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(null=True)

class Student(models.Model):
    collage=models.ForeignKey(Collage, on_delete=models.CASCADE , null=True)
    name= models.CharField(max_length=60)
    address= models.TextField(max_length=180)
    created_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(null=True)
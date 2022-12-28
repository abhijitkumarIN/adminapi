from django.db import models

# Create your models here.
class School(models.Model):
    nama= models.CharField(max_length=130)
    roll= models.IntegerField()
    city = models.CharField(max_length=290)
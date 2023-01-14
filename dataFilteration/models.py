from django.db import models

# Create your models here.


class LatestProducts(models.Model):
    name = models.CharField(max_length=200),
    describition = models.TextField(max_length=400)
    price = models.CharField(max_length=90 ,null=False)
    


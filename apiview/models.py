from django.db import models

# Create your models here.

class RecurrringOrder(models.Model):
    name = models.CharField(max_length=80)
    title = models.CharField(max_length=90)
    pricing = models.CharField(max_length=70)
    
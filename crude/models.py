from django.db import models

# Create your models here

NOTITFICATION_TYPE = (
    ("Web", "Web"),
    ("android", "android"),
    ("iphone", "iphone")
)
NOTITFICATION_STATUS = (
    ("Pending", "Pending"),
    ("Sent", "Sent"),
    ("Delivered", "Delivered"),
    ("Seen", "Seen")
)


class Notification(models.Model):
    subject = models.CharField(max_length=20)
    describition = models.CharField(max_length=200)
    status = models.CharField(choices=NOTITFICATION_STATUS , max_length=50)
    notification_type = models.CharField(choices=NOTITFICATION_TYPE , max_length=70)
    senting_time = models.DateField(auto_now=True)
    created_At = models.DateField(auto_now=True)

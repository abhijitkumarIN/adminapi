from django.core.mail import send_mail
import math , random

def sendMail(subject , message ,from_email , to):
  
    send_mail(
        subject,
        message,
        from_email ,
        [to],
        fail_silently=False,
    )

def otpGenerator():
    num = "0123456789"
    otp=""
    for x in range(4):
         otp += num[math.floor(random.random* len(num))]
         return otp

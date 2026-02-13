from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.conf.global_settings import EMAIL_HOST_USER


def SendMail():
    subject = "Welcome to Todo application"
    message = "Blah blah blah blah blah blah blah blah"
    email = User.email
    
    send_mail(
        subject=subject,
        message=message,
        from_email=EMAIL_HOST_USER,
        recipient_list = email,
        fail_silently=True
    )
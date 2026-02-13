from django.db import models
from django.contrib.auth.models import User


GENDER_CHOICES = (
                  ('M','Male'),
                  ('F', 'Female'),
                  ('O','Other')
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=50)
    gender = models.CharField(max_length=50, choices = GENDER_CHOICES)
    profile_pix = models.ImageField(upload_to = 'profile_pix')

    def __str__(self):
        return f'welcome back {self.user.username}'
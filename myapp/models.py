from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# User models that includes employee and employers
class User(AbstractUser):
    fullname = models.CharField(max_length=255)
    is_email_verified = models.BooleanField(default=False)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(unique=True, max_length=25)

    # log in with email instead of username
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
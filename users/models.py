from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.utils import timezone


# Create your models here.
class CustomUserManager(UserManager):
    pass

class CustomUser(AbstractUser):
    objects = CustomUserManager()

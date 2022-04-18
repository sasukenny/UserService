from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import PermissionsMixin, User
from django.db.models.signals import post_save

# Create your models here.
class Usuario(AbstractBaseUser):
    name = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
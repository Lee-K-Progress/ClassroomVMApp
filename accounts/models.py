"""
Lee Kusowski
ClassroomVMApp
Feb 04 2026
"""

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as lazytxt

from .managers import CustomUserManager

class CustomUser(AbstractUser):
    '''
    Custom User for ClassroomVMApp Project

    Users need:
        Email
        Password
    '''

    username = None
    email = models.EmailField(lazytxt("email address"), unique=True)
    first_name = models.CharField()
    last_name = models.CharField()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    def get_absolute_url(self):
        """Get Absolute URL for CustomUser model"""
        return reverse("account_detail", kwargs={"id": self.email})
    
    def __str__(self):
        """CustomUser String Method"""
        return self.last_name

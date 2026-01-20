# Lee Kusowski
# Webhooks
# Dec 05 2025

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

class CustomUser(AbstractUser):
    '''Custom User for {my_project} Project'''

    # Users need:
    # Username
    # Password
    # Email
    # 

    def get_absolute_url(self):
        """Get Absolute URL for CustomUser model"""
        return reverse("account_detail", kwargs={"id": self.id})
    
    def __str__(self):
        """CustomUser String Method"""
        return str(self.username)
    
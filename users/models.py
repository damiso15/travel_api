"""Users model."""

from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """Custom users."""

    password = models.CharField(blank=True, max_length=255)
    gender = models.CharField(blank=True, max_length=255)
    dob = models.CharField(blank=True, max_length=255)
    profile_img = models.FileField(blank=False, null=True)

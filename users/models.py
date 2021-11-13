from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    pass


class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="profile")
    profile_pic = models.FileField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)

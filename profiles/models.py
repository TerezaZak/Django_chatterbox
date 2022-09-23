from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about_me = models.TextField(null=True)
    photo = models.TextField(null=True)
    last_seen = models.DateTimeField(auto_now=True)
    signed_up = models.DateTimeField(auto_now_add=True)

class OnLineUsers(models.Model):
    logged = models.OneToOneField(User, on_delete=models.CASCADE)



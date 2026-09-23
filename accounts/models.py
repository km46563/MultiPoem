from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Profile(models.Model):
    description = models.TextField(blank=True)
    # TODO: Here will be some kind of background; gradient or png/jpg, I don't know yet
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

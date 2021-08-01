from django.db import models
from django.contrib.auth.models import AbstractUser


class CostumUser(AbstractUser):
    """This model override the 'django user model' that we can work on it"""
    def __str__(self):
        return self.username

from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """This model override the 'django user model' that we can work on it"""
    date_of_birth = models.DateField(default=None, null=True)

    def __str__(self):
        return self.username

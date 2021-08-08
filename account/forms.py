from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from django.db import models


class SignInForm(UserCreationForm):
    """Create form for sign_in"""
    username = forms.CharField()
    email = forms.EmailField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

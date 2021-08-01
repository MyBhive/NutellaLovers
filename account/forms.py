from django import forms
from .models import CostumUser
from django.contrib.auth.forms import UserCreationForm


class SignInForm(UserCreationForm):
    """Create form for sign_in"""
    username = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = CostumUser
        fields = ['username', 'email', 'password1', 'password2']

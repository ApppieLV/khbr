from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email',
                'password']

class SignInUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
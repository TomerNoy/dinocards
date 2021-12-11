from django import forms
from django.contrib.auth.forms import UserCreationForm

from . models import *


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profileType']

        labels = {
            'profileType': 'Profile type'
        }

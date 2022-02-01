from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django.forms import fields
from django.forms.widgets import EmailInput

from .models import Profile, Sonnet

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    #configurations
    class Meta:
        model = User
        fields = ['username', 'email','password1','password2']
        

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

# class WritePoem(forms.ModelForm):
#     class Meta:
#         model = Sonnet
#         fields = ['title','poem']
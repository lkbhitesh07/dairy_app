import datetime
from django import forms
from .models import *
from django.forms import ModelForm
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('user', 'first_name', 'last_name', 'contact_no', 'time', 'address', 'joining_date')

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=30, help_text='Your choice', required=False)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name','email', 'password1', 'password2')
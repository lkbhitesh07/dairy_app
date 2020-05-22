import datetime
from django import forms
from .models import *
from django.forms import ModelForm
from django.shortcuts import render

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('user', 'first_name', 'last_name', 'contact_no', 'time', 'address', 'joining_date')

class SignupForm(forms.Form):

    def signup(self, request, user):
        template_name = 'my_dairy/add_customer.html'
        return render(request, template_name)
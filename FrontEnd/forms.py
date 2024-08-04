from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

class Register_User_Form(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        
    
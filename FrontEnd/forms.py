from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

class Register_Form(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
    
    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['username']
        user.set_password(self.cleaned_data['password'])
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['username']
        user.set_password(self.cleaned_data['password'])
        user.email = self.cleaned_data['email']
        
        if commit:
            user.save()
        return user
        
class Login_Form(forms.Form):
    username = forms.CharField(max_length=30, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    
    
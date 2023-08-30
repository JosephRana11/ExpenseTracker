from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
  class Meta:
    model = User
    fields = ['username' , 'email' , 'password1' , 'password2']

class LoginForm(forms.Form):
  username = forms.CharField(max_length=50)
  password = forms.CharField(max_length=100 , widget=forms.PasswordInput)
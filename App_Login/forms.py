from django.forms import ModelForm
from django import forms
from App_Login.models import User, Profile

from django.contrib.auth.forms import UserCreationForm


# forms

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)

class SignUpForm(UserCreationForm):
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'email-field','placeholder': 'Email'}), label='')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'password-field','placeholder': 'Password'}), label='')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'password-field','placeholder': 'Confirm password'}), label='',)
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2',)
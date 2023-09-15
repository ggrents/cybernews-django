from captcha.fields import CaptchaField
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from .models import *


class CreateUser(UserCreationForm):
    captcha = CaptchaField()
    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={'class': ' form-input'}))
    password1 = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={'class': 'form-input'}),
    )
    password2 = forms.CharField(
        label="Подтвердите пароль",
        widget=forms.PasswordInput(attrs={'class': 'form-input'}),
    )

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']



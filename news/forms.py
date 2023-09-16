from captcha.fields import CaptchaField
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from .models import *


class AddArticle(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Article
        fields = ['title', 'tags', 'text', 'image', 'category']


class SearchForm(forms.Form):
    query = forms.CharField(label='Поиск', max_length=100)


class AddComment(forms.ModelForm):
    text = forms.CharField(widget=forms.TextInput(attrs={'size': '30', 'style': 'height: 40px;'}))
    class Meta:
        model = Comment
        fields = "__all__"
        exclude = ['article', 'author', 'name']

class CreateUser(UserCreationForm) :
    captcha = CaptchaField()
    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={'class' : ' form-input' }))
    password1 = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={'class': 'form-input'}),
    )
    password2 = forms.CharField(
        label="Подтвердите пароль",
        widget=forms.PasswordInput(attrs={'class': 'form-input'}),
    )
    class Meta :
        model = User
        fields = ['username', 'password1', 'password2']
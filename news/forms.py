from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from .models import *


class AddArticle(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'text', 'image', 'category']


class AddComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = "__all__"
        exclude = ['article']

class CreateUser(UserCreationForm) :
    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={'class' : ' form-input' }))
    password1 = forms.CharField(label="Пароль", widget=forms.TextInput(attrs={'class' : ' form-input' }))
    password2 = forms.CharField(label="Потвердите Пароль", widget=forms.TextInput(attrs={'class' : ' form-input' }))
    class Meta :
        model = User
        fields = ['username', 'password1', 'password2']
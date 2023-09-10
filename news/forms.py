from django import forms
from django.forms import ModelForm

from .models import *

class AddArticle(forms.ModelForm) :
    class Meta :
        model = Article
        fields = ['author', 'title', 'text', 'image', 'category']


class RandomForm(forms.Form) :
    name = forms.CharField()
    surname = forms.CharField()

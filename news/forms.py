from django import forms
from .models import User, Category


class FormCategories(forms.Form):
    name = forms.CharField(max_length=200)

from django import forms
from .models import User, Category


class FormCategories(forms.Form):
    name = forms.CharField(max_length=200)


class FormNews(forms.Form):
    title = forms.CharField(max_length=200)
    content = forms.CharField(widget=forms.Textarea)
    author = forms.ModelChoiceField(queryset=User.objects.all())
    created_at = forms.DateField()
    image = forms.ImageField()
    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all()
        )

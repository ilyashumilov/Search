from django import forms
from .models import client

class searchform(forms.Form):
    name = forms.CharField(label='Name', widget=forms.TextInput(attrs={'id': 'search', 'placeholder': 'Search','autocomplete':"off"}))


from django import forms

class SearchForm(forms.Form):
    topic = forms.CharField(max_length=100)
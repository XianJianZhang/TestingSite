from django import forms

class SimpleForm(forms.Form):
  name = forms.TextField(max_length=100)
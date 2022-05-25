from django import forms
from django.core import validators

class GuessForm(forms.Form):
    guess = forms.CharField(validators=[
        validators.MaxLengthValidator(5, "Please guess a 5 letter word"),
        validators.MinLengthValidator(5, "Please guess a 5 letter word")
    ])
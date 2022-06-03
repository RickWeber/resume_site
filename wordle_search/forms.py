from django import forms
from django.core import validators
from django.forms.widgets import HiddenInput

class GuessForm(forms.Form):
    guess = forms.CharField(validators=[
        validators.MaxLengthValidator(5, "Please guess a 5 letter word"),
        validators.MinLengthValidator(5, "Please guess a 5 letter word")
    ])
    previous_guesses = forms.CharField(widget=forms.HiddenInput())
#    previous_flags = forms.CharField(widget=forms.HiddenInput())
#    guess1 = forms.CharField(widget=forms.HiddenInput())
#    guess2 = forms.CharField(widget=forms.HiddenInput())
#    guess3 = forms.CharField(widget=forms.HiddenInput())
#    guess4 = forms.CharField(widget=forms.HiddenInput())
#    guess5 = forms.CharField(widget=forms.HiddenInput())
#    guess6 = forms.CharField(widget=forms.HiddenInput())
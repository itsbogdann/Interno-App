from django import forms

from django.core.validators import RegexValidator

my_validator = RegexValidator("\d{4}", "Trebuie introdus un an.")

from .models import Contract


class LoginForm(forms.Form):
    username = forms.CharField(label="Nume")
    password = forms.CharField(label="Parola", widget=forms.PasswordInput)


class StatisticiForm(forms.Form):
    an = forms.CharField(label="")
    validators=[my_validator]


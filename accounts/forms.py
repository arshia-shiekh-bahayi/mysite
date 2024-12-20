from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=200)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class Email_AuthenticationForm(forms.Form):
    username = forms.EmailField()
    password = forms.CharField()


class ResetPasswordForm(forms.Form):
    email = forms.EmailField()

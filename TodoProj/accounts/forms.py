from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20, label="", widget=forms.TextInput(attrs=({
                'class':'form-control',
                'placeholder':'Please enter Username',
    })))
    password = forms.CharField(max_length=20, label="", widget=forms.PasswordInput(attrs=({
                    'class':'form-control',
                    'placeholder':'Please enter Password',
    })))

class UserRegisterForm(forms.Form):
    username = forms.CharField(max_length=20, label="", widget=forms.TextInput(attrs=({
                'class':'form-control',
                'placeholder':'Please enter Username',
    })))
    password = forms.CharField(max_length=20, label="", widget=forms.PasswordInput(attrs=({
                    'class':'form-control',
                    'placeholder':'Please enter Password',
    })))
    control_password = forms.CharField(max_length=20, label="", widget=forms.PasswordInput(attrs=({
                    'class':'form-control',
                    'placeholder':'Please enter Password again',
    })))

    def clean_username(self):
        cuser = self.cleaned_data['username']
        qs = User.objects.filter(username=cuser)
        if qs.exists():
            raise ValidationError("Username already exists!")
        return cuser

    def clean_password(self):
        cpassword = self.cleaned_data["password"]
        if len(cpassword) < 5:
            raise ValidationError("Password has to be at least 5 characters long")
        return cpassword

    def clean(self):
        cleaned_data = super().clean()
        pass1 = cleaned_data.get('password')
        pass2 = cleaned_data.get('control_password')

        if pass1 != pass2:
            print('Password did not match')
            raise ValidationError('Passwords did not match')

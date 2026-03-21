from django import forms
from .models import User


class RegisterForm(forms.ModelForm):
    password = forms.CharField(
        max_length=250,
        widget=forms.PasswordInput(
            attrs={"class": "inp", "placeholder": "Enter Strong Password..."}
        ),
    )
    confirm_password = forms.CharField(
        max_length=250,
        widget=forms.PasswordInput(
            attrs={"class": "inp", "placeholder": "Must equal Password..."}
        ),
    )

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "phone",
            "address",
            "password",
        ]
        widgets = {
            "username": forms.TextInput(
                attrs={"class": "inp", "placeholder": "Enter username..."}
            ),
            "email": forms.EmailInput(
                attrs={"class": "inp", "placeholder": "example@gmail.com"}
            ),
            "phone": forms.TextInput(
                attrs={"class": "inp", "placeholder": "Enter your phone number..."}
            ),
            "address": forms.TextInput(
                attrs={"class": "inp", "placeholder": "Enter your address..."}
            ),
        }

    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get("password")
        confirm = cleaned_data.get("confirm_password")

        if password != confirm:
            raise forms.ValidationError("Pass do not match")

        return cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=250,
        widget=forms.TextInput(
            attrs={"class": "inp", "placeholder": "Enter username..."}
        ),
    )
    password = forms.CharField(
        max_length=250,
        widget=forms.PasswordInput(
            attrs={"class": "inp", "placeholder": "Enter Strong Password..."}
        ),
    )

from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from application.models import UserInfo

class RegistrationForm(forms.Form):

    username = forms.CharField(
        max_length=150,
        label="Felhasználónév",
        error_messages={
            "required": "A felhasználónév kitöltése kötelező!",
            "invalid": "Felhasználónév: csak betűk, számok és @/./+/-/_ karakterek engedélyezettek!",
            "max_length": "A felhasználónév nem lehet hosszabb, mint 150 karakter!"
        }
    )
    email = forms.EmailField(
        label="E-mail",
        error_messages={
            "required": "Az email kitöltése kötelező!",
            "invalid": "Helytelen email formátum!",
        }
    )
    password = forms.CharField(
        widget=forms.PasswordInput,
        label="Jelszó",
        min_length=8,
        error_messages={
            "required": "A jelszó kitöltése kötelező!",
            "min_length": "A jelszónak legalább 8 karakter hosszúnak kell lennie!",
        }
    )
    first_name = forms.CharField(
        max_length=255,
        label="Keresztnév",
        error_messages={
            "required": "A keresztnév kitöltése kötelező!",
        }
    )
    last_name = forms.CharField(
        max_length=255,
        label="Vezetéknév",
        error_messages={
            "required": "A vezetéknév kitöltése kötelező!",
        }
    )
    address = forms.CharField(
        max_length=255,
        label="Cím",
        error_messages={
            "required": "A cím kitöltése kötelező!",
        }
    )
    birth_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label="Születési dátum",
        error_messages={
            "required": "Dátum kitöltése kötelező!",
            "invalid": "Érvénytelen dátum formátum!",
        }
    )
    phone_number = forms.CharField(
        label="Telefonszám",
        min_length=11,
        max_length=12,
        error_messages={
            "required": "A telefonszám kitöltése kötelező!",
            "min_length": "A telefonszám nem lehet rövidebb, mint 11 karakter!",
            "max_length": "A telefonszám nem lehet hosszabb, mint 12 karakter!",
        }
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError("Ez a felhasználónév már foglalt!")
        return username
    def clean_phone_number(self):
        phone_number = self.cleaned_data.get("phone_number")
        if UserInfo.objects.filter(phone_number=phone_number).exists():
            raise ValidationError("Ez a telefonszám már létezik!")
        return phone_number
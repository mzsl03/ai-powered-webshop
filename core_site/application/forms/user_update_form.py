from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.exceptions import ValidationError
from application.models import UserInfo

class UserUpdateForm(forms.ModelForm):
    
    username = forms.CharField(
        max_length=150,
        label="Felhasználónév",
        validators=[UnicodeUsernameValidator()],
        error_messages={
            'required': 'A felhasználónév kitöltése kötelező!',
            'invalid': 'Csak betűk, számok és @/./+/-/_ karakterek engedélyezettek!',
        }
    )

    email = forms.EmailField(
        label="E-mail",
        error_messages={
            "required": "Az email mező kitöltése kötelező!",
            "invalid": "Helytelen email formátum!",
        }
    )

    
    address = forms.CharField(
        max_length=255,
        label="Cím",
        required=False,
        error_messages={
            "required": "Cím mező kitöltése kötelező!",
        }
    )
    
    phone_number = forms.CharField(
        max_length=12,
        min_length=11,
        label="Telefonszám",
        required=False,
        error_messages={
            "required": "Telefonszám mező kitöltése kötelező!",
            "min_length": "A telefonszám legalább 11 karakter kell legyen!",
            "max_length": "A telefonszám legfeljebb 12 karakter kell legyen!",
        }
    )

    class Meta:
        model = User
        fields = ['username', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        if self.instance and hasattr(self.instance, 'phoneshop_user'):
            try:
                user_info = self.instance.phoneshop_user
            except UserInfo.DoesNotExist:
                user_info = None
            print(user_info)

            if user_info:
                self.fields['address'].initial = user_info.address
                self.fields['phone_number'].initial = user_info.phone_number


    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exclude(pk=self.instance.pk).exists():
            raise ValidationError('Ez a felhasználónév már foglalt!')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise ValidationError('Ezzel az email címmel már regisztráltak!')
        return email
        
    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if phone_number and UserInfo.objects.filter(phone_number=phone_number).exclude(user=self.instance).exists():
            raise ValidationError('Ez a telefonszám már foglalt!')
        return phone_number


    def save(self, commit=True):
        user = super().save(commit=commit)

        user_info, created = UserInfo.objects.get_or_create(user=user)

        user_info.address = self.cleaned_data.get('address')
        user_info.phone_number = self.cleaned_data.get('phone_number')

        if commit:
            user_info.save()

        return user
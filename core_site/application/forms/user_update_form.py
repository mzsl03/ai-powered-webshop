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
            'invalid': 'Csak betűk, számok és @/./+/-/_ karakterek engedélyezettek.',
            'unique': 'Ez a felhasználónév már foglalt.'
        }
    )

    email = forms.EmailField(
        label="E-mail",
        error_messages={'invalid': 'Helytelen e-mail formátum.'}
    )

    first_name = forms.CharField(max_length=255, label="Keresztnév")
    last_name = forms.CharField(max_length=255, label="Vezetéknév")

    address = forms.CharField(max_length=255, label="Cím")
    phone_number = forms.CharField(max_length=12, label="Telefonszám")

    class Meta:
        model = User
        fields = ['username', 'email']
        labels = {
            'username': 'Felhasználónév',
            'email': 'E-mail cím'
        }
        help_texts = {
            'username': 'Csak betűk, számok és @/./+/-/_ karakterek engedélyezettek.'
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.get('instance')
        super().__init__(*args, **kwargs)

        if user and hasattr(user, 'userinfo'):
            self.fields['address'].initial = user.userinfo.address
            self.fields['birth_date'].initial = user.userinfo.birth_date
            self.fields['phone_number'].initial = user.userinfo.phone_number

    def save(self, commit=True):
        user = super().save(commit=False)
        user_info, created = UserInfo.objects.get_or_create(user=user)
        user_info.address = self.cleaned_data.get('address')
        user_info.birth_date = self.cleaned_data.get('birth_date')
        user_info.phone_number = self.cleaned_data.get('phone_number')

        if commit:
            user.save()
            user_info.save()
        return user

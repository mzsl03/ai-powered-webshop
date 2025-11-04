from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.validators import UnicodeUsernameValidator
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

    email = forms.EmailField(label="E-mail", required=True)
    address = forms.CharField(max_length=255, label="Cím", required=False)
    phone_number = forms.CharField(max_length=12, label="Telefonszám", required=False)

    class Meta:
        model = User
        fields = ['username', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        user = self.instance
        if hasattr(user, 'phoneshop_user'):
            self.fields['address'].initial = user.phoneshop_user.address
            self.fields['phone_number'].initial = user.phoneshop_user.phone_number

    def save(self, commit=True):
        user = super().save(commit=commit)
        user_info, _ = UserInfo.objects.get_or_create(user=user)
        address = self.cleaned_data.get('address')
        if address is not None and address.strip() != '':
            user_info.address = address

        phone = self.cleaned_data.get('phone_number')
        if phone is not None and phone.strip() != '':
            user_info.phone_number = phone

        if commit:
            user_info.save()

        return user

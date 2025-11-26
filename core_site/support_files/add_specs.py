from django import forms
from django.contrib.postgres.forms import SimpleArrayField
import re
from application.models import Specs
from django.core.exceptions import ValidationError



class SpecsForm(forms.ModelForm):
    class Meta:
        model = Specs
        fields = [
            'CPU_speed', 'CPU_type', 'display_size', 'resolution',
            'display_technology', 'max_refresh_rate', 'Spen', 'camera',
            'memory', 'storage', 'os', 'charge', 'sensors',
            'size', 'weight', 'battery', 'release_date'
        ]

    CPU_speed = forms.CharField(
        label = "CPU sebesség",
        error_messages = {
            "required": "CPU sebesség kitöltése kötelező!"
        }
    )

    CPU_type = forms.CharField(
        label = "CPU típus",
        error_messages = {
            "required": "CPU típus kitöltése kötelező!"
        }
    )

    display_size = forms.CharField(
        label = "Kijelző méret",
        error_messages = {
            "required": "Kijelző méret kitöltése kötelező!"
        }
    )

    resolution = forms.CharField(
        label = "Felbontás",
        error_messages = {
            "required": "Felbontás kitöltése kötelező!"
        }
    )

    display_technology = forms.CharField(
        label = "Kijelző technológia",
        error_messages = {
            "required": "Kijelző technológia kitöltése kötelező!"
        }
    )
    
    max_refresh_rate = forms.CharField(
        label="Max frissítési gyakoriság",
        error_messages = {
            "required": "Max frissítési gyakoriság kitöltése kötelező!"
        }
    )

    Spen = forms.BooleanField(
        label="S Pen",
        required=False
    )

    camera = forms.CharField(
        label="Kamera",
        error_messages = {
            "required": "Kamera kitöltése kötelező!"
        }
    )

    memory = SimpleArrayField(
        forms.IntegerField(
            min_value=1,
            error_messages={
                "invalid": "Csak egész számot adhatsz meg!"
            }),
        label="Memória",
        error_messages={
            "required": "Memória kitöltése kötelező!",
            "item_invalid": "Vesszővel elválasztva írja be az egész számokat!",
        },
        help_text="Add meg a számokat vesszővel elválasztva (pl. 8,16,32)."
    )

    storage = SimpleArrayField(
        forms.IntegerField(
            min_value=1,
            error_messages={
                "invalid": "Csak egész számot adhatsz meg!"
            }),
        label="Tárhely",
        error_messages={
            "required": "Tárhely kitöltése kötelező!",
            "item_invalid": "Vesszővel elválasztva írja be az egész számokat!",
        },
        help_text="Add meg a számokat vesszővel elválasztva (pl. 64,128,256)."
    )

    os = forms.CharField(
        label="Operációs rendszer",
        error_messages = {
            "required": "Operációs rendszer kitöltése kötelező!"
        }
    )
    
    charge = forms.CharField(
        label="Töltés",
        error_messages = {
            "required": "Töltés kitöltése kötelező!"
        }
    )

    sensors = forms.CharField(
        label="Szenzorok",
        error_messages = {
            "required": "Szenzorok kitöltése kötelező!"
        }
    )
    
    size = forms.CharField(
        label="Méret",
        error_messages = {
            "required": "Méret kitöltése kötelező!"
        }
    )
    
    weight = forms.FloatField(
        label="Súly",
        widget=forms.TextInput(attrs={'placeholder': 'pl. 10.5'}),
        error_messages={
            "required": "Súly kitöltése kötelező!",
            "invalid": "Csak számot adhatsz meg (pl. 10 vagy 10.5)!"
        }
    )
    
    battery = forms.IntegerField(
        label = "Akkumulátor",
        widget = forms.TextInput,
        error_messages = {
            "required": "Akkumulátor kitöltése kötelező!",
            "invalid": "Csak egész számot adhatsz meg!"
        }
    )
    
    release_date = forms.DateField(
        label="Kiadási dátum",
        error_messages={
            "required": "Kiadási dátum kitöltése kötelező!"
        }
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance and self.instance.pk and 'memory' in self.initial and 'storage' in self.initial:

            raw_data_memory = self.initial["memory"]
            raw_data_storage = self.initial["storage"]

            if isinstance(raw_data_memory, list):
                self.initial['memory'] = ",".join([str(x) for x in raw_data_memory])
            elif isinstance(raw_data_memory, str):
                cleaned_memory = raw_data_memory.replace('[', '').replace(']', '').replace("'", "").replace('"', "")
                self.initial['memory'] = cleaned_memory

            if isinstance(raw_data_storage, list):
                self.initial['storage'] = ",".join([str(x) for x in raw_data_storage])
            elif isinstance(raw_data_storage, str):
                cleaned_storage = raw_data_storage.replace('[', '').replace(']', '').replace("'", "").replace('"', "")
                self.initial['storage'] = cleaned_storage
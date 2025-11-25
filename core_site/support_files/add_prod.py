from django import forms
from application.models import Products, Specs
from django.utils.text import slugify
from django.core.exceptions import ValidationError



class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['name', 'price', 'category', 'colors', 'image_path', "stock"]
        widgets = {
            'image_path': forms.HiddenInput(),
            "stock": forms.HiddenInput()
        }
        
    CATEGORIES = (
        ("", "Válassz kategóriát..."),
        ("Telefon", "Telefon"),
        ("Tartozék", "Tartozék")
    )
    
    name = forms.CharField(
        max_length=255,
        label="Termék neve",
        error_messages={
            "required": "Termék nevének megadása kötelező!",
        }
    )

    price = forms.IntegerField(
        label="Ár",
        widget=forms.TextInput,
        error_messages={
            "required": "Ár kitöltése kötelező!",
            "invalid": "Csak egész számot adhat meg!",
        }
    )

    category = forms.ChoiceField(
        choices=CATEGORIES,
        label="Kategória",
        error_messages={
            "required": "Kategória választása kötelező",
            "invalid_choice": "A listából válaszd ki a kategóriát"
        }
    )

    colors = forms.CharField(
        label="Színek (vesszővel elválasztva)",
        error_messages={
            "required": "Színek megadása kötelező"
        }
    )


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        if self.instance and self.instance.pk and 'colors' in self.initial:
            
            raw_data = self.initial['colors']
            
            if isinstance(raw_data, list):
                self.initial['colors'] = ",".join(raw_data)
                
            elif isinstance(raw_data, str):
                cleaned = raw_data.replace('[', '').replace(']', '').replace("'", "").replace('"', "")
                self.initial['colors'] = cleaned

    def clean_name(self):
        name = self.cleaned_data.get('name')

        qs = Products.objects.filter(name=name)
        
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
    
        if qs.exists():
            raise ValidationError("Ez a termék már létezik!")
        return name


    def clean_colors(self):
        colors_string = self.cleaned_data.get('colors')

        if not colors_string:
            raise ValidationError("Legalább egy érvényes színt meg kell adni.")
        
        colors_list = [color.strip() for color in colors_string.split(',') if color.strip()]

        if not colors_list:
            raise ValidationError("Legalább egy érvényes színt meg kell adni.")
            
        FORBIDDEN_CHARS = [' ', ';', '.', '-']

        validated_list = []
        
        for color in colors_list:
            if color.isdigit():
                raise ValidationError(f"A '{color}' helyett egy érvényes színt adjon meg!")
            found_bad_char = False
            for char in FORBIDDEN_CHARS:
                if char in color:
                    if char == ' ':
                        raise ValidationError(
                            f"A '{color}' színnév szóközt tartalmaz. Kérlek, írd egybe (pl. '{color.replace(' ', '')}')."
                        )
                    else:
                        raise ValidationError(
                            f"A '{color}' színnév érvénytelen karaktert ('{char}') tartalmaz. Kérlek, távolítsd el."
                        )
                    found_bad_char = True
                    break
            
            if not found_bad_char:
                validated_list.append(color)

        return validated_list

    

    def save(self, commit=True):
        instance = super().save(commit=False)
        slug_name = slugify(self.cleaned_data['name'])
        colors = self.cleaned_data.get('colors', [])

        if self.cleaned_data["category"] == "Tartozék":
            instance.stock = [10] * len(colors)
            
        elif self.cleaned_data["category"] == "Telefon":
            if self.instance.pk:
                specs = Specs.objects.get(product_id=self.instance.pk)
                times = len(specs.memory) * len(colors)
                instance.stock = [10] * times
            else:
                instance.stock = []

        instance.image_path = [f"{slug_name}-{color.lower()}.png" for color in colors]

        if commit:
            instance.save()
        return instance

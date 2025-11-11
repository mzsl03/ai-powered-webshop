from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User


class Products(models.Model):
    categories = (
        ("Telefon", "Telefon"),
        ("Tartozék", "Tartozék")
    )

    name = models.CharField(max_length=255)
    price = models.IntegerField()
    category = models.CharField(choices=categories, default='Telefon')
    colors = ArrayField(
        models.CharField(max_length=50),
        blank=False,
        default=list
    )
    image_path = ArrayField(
        models.CharField(max_length=255),
        blank=True,
        default=list
    )
    stock = ArrayField(
        models.IntegerField(),
        blank=True,
        default=list
    )

    def __str__(self):
        return f"{self.name}"
    

class Specs(models.Model):
    product = models.OneToOneField(
        Products,
        on_delete=models.CASCADE,
        related_name='specs'
    )

    CPU_speed = models.CharField(max_length=255)
    CPU_type = models.CharField(max_length=255)
    display_size = models.CharField(max_length=255)
    resolution = models.CharField(max_length=255)
    display_technology = models.CharField(max_length=255)
    max_refresh_rate = models.CharField(max_length=255)
    Spen = models.BooleanField(default=False)
    camera = models.CharField(max_length=255)
    memory = ArrayField(
        models.IntegerField(),
        blank=False,
        default=list
    )
    storage = ArrayField(
        models.IntegerField(),
        blank=False,
        default=list
    )
    os = models.CharField(max_length=255)
    charge = models.CharField(max_length=255)
    sensors = models.CharField(max_length=255)
    size = models.CharField(max_length=255)
    weight = models.IntegerField()
    battery = models.IntegerField()
    release_date = models.DateField()

    def __str__(self):
        return f"{self.product.name} specifikációs adatai"

class Orders(models.Model):
    STATUS_CHOICES = (
        ("feldolgozás_alatt", "Feldolgozás alatt"),
        ("kiszállítva", "Kiszállítva"),
        ("törölve", "Törölve"),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    order_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="feldolgozás_alatt")

    def __str__(self):
        return f"{self.user.username} rendelése ({self.get_status_display()})"

class OrderItem(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    color = models.CharField(max_length=255)
    storage = models.IntegerField(null=True, blank=True)
    price = models.IntegerField()

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"

class UserInfo(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='phoneshop_user',
        null=False,
        blank=False
    )
    address = models.CharField(max_length=255)
    birth_date = models.DateField()
    phone_number = models.CharField(max_length=12)

    
    def __str__(self):
        return f"{self.user}"


class Sales(models.Model):
    order = models.OneToOneField(
        Orders,
        on_delete=models.CASCADE,
        related_name='sale')
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='sales')
    product = models.ForeignKey(
        Products,
        on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()
    color = models.CharField(max_length=255)
    storage = models.IntegerField(null=True, blank=True)
    tax_number = models.CharField(max_length=10)
    selling_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Számla: {self.user.username} ({self.selling_time.strftime('%Y-%m-%d')})"


class Cart(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='cart'
    )
    product = models.ForeignKey(
        Products,
        on_delete=models.CASCADE,
        related_name='cart'
    )
    
    quantity = models.IntegerField()
    price = models.IntegerField()
    color = models.CharField(max_length=255)
    storage = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.user} felhasználónak kosárban levő termékei"

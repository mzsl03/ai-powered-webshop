from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from django.utils import timezone
from unittest.mock import patch, MagicMock


class ProductMock:
    def __init__(self, name="Test Product", price=1000):
        self.name = name
        self.price = price


class CartItemMock:
    def __init__(self, product, quantity, color="Red", storage="128GB", price=1000):
        self.product = product
        self.quantity = quantity
        self.color = color
        self.storage = storage
        self.price = price


class OrdersMock:
    def __init__(self, user, status, order_time):
        self.user = user
        self.status = status
        self.order_time = order_time
        self.id = 1

class OrderItemMock:
    pass


class CheckoutViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.checkout_url = reverse('checkout')
        self.cart_url = reverse('cart')
        self.user_order_url = reverse('user_order')
        self.login_required_redirect = '/'

        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

        self.product_a = ProductMock(name="Product A", price=5000)

        self.cart_items_data = [
            CartItemMock(product=self.product_a, quantity=2, price=5000, color="Red"),  # Összesen 10000
        ]

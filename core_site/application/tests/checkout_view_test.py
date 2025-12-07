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

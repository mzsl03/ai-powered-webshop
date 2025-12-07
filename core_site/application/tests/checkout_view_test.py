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

    def test_access_denied_if_not_logged_in(self):
        response = self.client.get(self.checkout_url)

        expected_redirect = f'{self.login_required_redirect}?next={self.checkout_url}'
        self.assertRedirects(response, expected_redirect)

    @patch('application.views.Cart.objects')
    def test_empty_cart_redirects_with_warning(self, MockCartManager):
        self.client.force_login(self.user)

        MockCartManager.filter.return_value.exists.return_value = False

        response = self.client.get(self.checkout_url, follow=True)

        self.assertRedirects(response, self.cart_url)

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "A kosár üres, nincs mit leadni.")
        self.assertEqual(messages[0].level_tag, 'warning')


    @patch('application.views.Orders.objects')
    @patch('application.views.OrderItem.objects')
    @patch('application.views.Cart.objects')
    def test_successful_checkout_process(self, MockCartManager, MockOrderItemManager, MockOrdersManager):
        self.client.force_login(self.user)

        mock_cart_items = MagicMock()
        mock_cart_items.exists.return_value = True
        mock_cart_items.__iter__.return_value = iter(self.cart_items_data)  # Iterálás a mock adatokon
        MockCartManager.filter.return_value = mock_cart_items

        created_order = OrdersMock(user=self.user, status="feldolgozás_alatt", order_time=timezone.now())
        MockOrdersManager.create.return_value = created_order

        response = self.client.get(self.checkout_url, follow=True)

        self.assertRedirects(response, self.user_order_url)

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), "Rendelésed sikeresen leadva!")
        self.assertEqual(messages[0].level_tag, 'success')

        MockOrdersManager.create.assert_called_once()
        self.assertEqual(MockOrdersManager.create.call_args[1]['user'], self.user)
        self.assertEqual(MockOrdersManager.create.call_args[1]['status'], "feldolgozás_alatt")

        self.assertEqual(MockOrderItemManager.create.call_count, len(self.cart_items_data))

        expected_price = self.cart_items_data[0].price * self.cart_items_data[0].quantity  # 5000 * 2 = 10000
        MockOrderItemManager.create.assert_called_once_with(
            order=created_order,
            product=self.product_a,
            quantity=2,
            color="Red",
            storage="128GB",
            price=expected_price,
        )

        mock_cart_items.delete.assert_called_once()
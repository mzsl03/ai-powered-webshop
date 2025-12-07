from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages

from application.models import Orders, Cart, Products, OrderItem, UserInfo
import datetime



class UserUpdateViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser",
            email="old@example.com",
            password="password123",
            first_name="Old",
            last_name="Name",
        )
        UserInfo.objects.create(
            user=self.user,
            address="Test address",
            birth_date=datetime.date(2000, 1, 1),
            phone_number="36123456789",
        )
        self.url = reverse("user_update")
        self.home_url = reverse("home")

    def test_user_update_get_prefilled_form(self):
        self.client.force_login(self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "update_user.html")
        self.assertIn("form", response.context)
        form = response.context["form"]
        self.assertEqual(form.instance, self.user)
        self.assertEqual(form.initial.get("email"), "old@example.com")

    def test_user_update_post_valid_updates_user_and_redirects(self):
        self.client.force_login(self.user)

        response = self.client.post(
            self.url,
            {
                "username": "testuser",
                "email": "new@example.com",
                "first_name": "New",
                "last_name": "Name",
                "address": "New address 123",
                "birth_date": "1995-05-10",
                "phone_number": "36301234567",
            },
            follow=True,
        )

        self.assertRedirects(response, self.home_url)

        self.user.refresh_from_db()

        self.assertEqual(self.user.username, "testuser")
        user_info = UserInfo.objects.get(user=self.user)
        self.assertEqual(user_info.address, "New address 123")
        self.assertEqual(user_info.phone_number, "36301234567")

    def test_user_update_requires_login(self):
        response = self.client.get(self.url)
        expected_redirect = f"/?next={self.url}"
        self.assertRedirects(response, expected_redirect)


class UserOrderViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="normal", password="pass")
        self.other_user = User.objects.create_user(username="other", password="pass")
        self.admin = User.objects.create_superuser(
            username="admin", password="adminpass", email="admin@example.com"
        )
        self.url = reverse("user_order")
        self.home_url = reverse("home")

        self.order_processing = Orders.objects.create(
            user=self.user, status="feldolgozás_alatt"
        )
        self.order_delivered = Orders.objects.create(
            user=self.user, status="kiszállítva"
        )
        self.order_deleted = Orders.objects.create(
            user=self.user, status="törölve"
        )
        self.other_order = Orders.objects.create(
            user=self.other_user, status="feldolgozás_alatt"
        )

    def test_user_order_lists_only_own_orders_grouped_by_status(self):
        self.client.force_login(self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "user_order.html")
        processing = list(response.context["processing"])
        delivered = list(response.context["delivered"])
        deleted = list(response.context["deleted"])
        self.assertIn(self.order_processing, processing)
        self.assertNotIn(self.other_order, processing)
        self.assertIn(self.order_delivered, delivered)
        self.assertIn(self.order_deleted, deleted)

    def test_user_order_redirects_for_superuser(self):
        self.client.force_login(self.admin)
        response = self.client.get(self.url)
        self.assertRedirects(response, self.home_url)

    def test_all_user_order_access(self):
        url = reverse("all_user_order")
        self.client.force_login(self.user)
        response = self.client.get(url)
        self.assertRedirects(response, self.home_url)
        self.client.force_login(self.admin)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "list_orders.html")
        orders = list(response.context["orders"])
        self.assertIn(self.order_processing, orders)
        self.assertIn(self.order_delivered, orders)
        self.assertIn(self.order_deleted, orders)
        self.assertIn(self.other_order, orders)
        self.assertEqual(orders[0].order_time >= orders[1].order_time, True)


class CheckoutViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="buyer", password="pass")
        self.checkout_url = reverse("checkout")
        self.cart_url = reverse("cart")
        self.user_order_url = reverse("user_order")

    def test_checkout_creates_order_and_clears_cart(self):
        product = Products.objects.create(
            name="Test Phone",
            price=100000,
            category="Telefon",
            colors=["black"],
            image_path=["test.jpg"],
            stock=[10],
        )
        Cart.objects.create(
            user=self.user,
            product=product,
            quantity=2,
            price=200000,
            color="black",
            storage=128,
        )
        self.client.force_login(self.user)
        response = self.client.post(self.checkout_url, follow=True)
        self.assertRedirects(response, self.user_order_url)
        orders = Orders.objects.filter(user=self.user)
        self.assertEqual(orders.count(), 1)
        order = orders.first()
        items = OrderItem.objects.filter(order=order)
        self.assertEqual(items.count(), 1)
        item = items.first()
        self.assertEqual(item.product, product)
        self.assertEqual(item.quantity, 2)
        self.assertFalse(Cart.objects.filter(user=self.user).exists())

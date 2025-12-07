from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages

from application.models import Orders, OrderItem, Products, Cart


class OrderModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="orderuser", password="pass")
        self.product = Products.objects.create(
            name="Model Phone",
            price=120000,
            category="Telefon",
            colors=["black"],
            image_path=["model.jpg"],
            stock=[10],
        )

    def test_order_str_uses_username_and_human_status(self):
        order = Orders.objects.create(user=self.user, status="kiszállítva")
        expected = f"{self.user.username} rendelése ({order.get_status_display()})"
        self.assertEqual(str(order), expected)

    def test_orderitem_str_includes_product_and_quantity(self):
        order = Orders.objects.create(user=self.user, status="feldolgozás_alatt")
        item = OrderItem.objects.create(
            order=order,
            product=self.product,
            quantity=3,
            color="black",
            storage=128,
            price=360000,
        )
        self.assertEqual(str(item), f"{self.product.name} x 3")


class OrderStatusUpdateViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="statususer", password="pass")
        self.admin = User.objects.create_superuser(
            username="admin",
            password="adminpass",
            email="admin@example.com",
        )
        self.order = Orders.objects.create(
            user=self.user,
            status="feldolgozás_alatt",
        )
        self.url = reverse("update_order_status", args=[self.order.id])
        self.all_orders_url = reverse("all_user_order")

    def test_update_order_status_valid_value_changes_status_and_redirects(self):
        self.client.force_login(self.admin)
        response = self.client.post(self.url, {"status": "kiszállítva"})
        self.assertRedirects(response, self.all_orders_url)
        self.order.refresh_from_db()
        self.assertEqual(self.order.status, "kiszállítva")

    def test_update_order_status_invalid_value_keeps_original_status(self):
        self.client.force_login(self.admin)
        response = self.client.post(self.url, {"status": "nem_letezo_status"})
        self.assertRedirects(response, self.all_orders_url)
        self.order.refresh_from_db()
        self.assertEqual(self.order.status, "feldolgozás_alatt")


class CheckoutOrderFlowTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="buyer", password="pass")
        self.checkout_url = reverse("checkout")
        self.user_order_url = reverse("user_order")
        self.cart_url = reverse("cart")

        self.product1 = Products.objects.create(
            name="Checkout Phone A",
            price=10000,
            category="Telefon",
            colors=["black"],
            image_path=["a.jpg"],
            stock=[10],
        )
        self.product2 = Products.objects.create(
            name="Checkout Phone B",
            price=20000,
            category="Telefon",
            colors=["white"],
            image_path=["b.jpg"],
            stock=[10],
        )

    def test_checkout_creates_order_and_items_and_clears_cart(self):
        Cart.objects.create(
            user=self.user,
            product=self.product1,
            quantity=1,
            price=self.product1.price,
            color="black",
            storage=128,
        )
        Cart.objects.create(
            user=self.user,
            product=self.product2,
            quantity=2,
            price=self.product2.price * 2,
            color="white",
            storage=256,
        )

        self.client.force_login(self.user)
        response = self.client.post(self.checkout_url, follow=True)

        self.assertRedirects(response, self.user_order_url)

        orders = Orders.objects.filter(user=self.user)
        self.assertEqual(orders.count(), 1)
        order = orders.first()

        items = OrderItem.objects.filter(order=order)
        self.assertEqual(items.count(), 2)

        item1 = items.get(product=self.product1)
        item2 = items.get(product=self.product2)
        self.assertEqual(item1.quantity, 1)
        self.assertEqual(item2.quantity, 2)

        self.assertFalse(Cart.objects.filter(user=self.user).exists())

    def test_checkout_requires_login_redirects_to_login(self):
        response = self.client.post(self.checkout_url)
        login_url = reverse("login")
        expected = f"{login_url}?next={self.checkout_url}"
        self.assertRedirects(response, expected)

    def test_checkout_empty_cart_redirects_to_cart_with_warning(self):
        self.client.force_login(self.user)
        response = self.client.post(self.checkout_url, follow=True)
        self.assertRedirects(response, self.cart_url)
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any("A kosár üres, nincs mit leadni." in str(m) for m in messages))

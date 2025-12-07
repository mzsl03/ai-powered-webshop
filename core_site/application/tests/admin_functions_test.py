from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from application.models import Products, Orders


class AddProductAdminAccessTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse("add_product")
        self.home_url = reverse("home")

    def test_add_product_get_superuser_can_access(self):
        admin = User.objects.create_superuser(
            username="admin",
            password="adminpass",
            email="admin@example.com",
        )
        self.client.force_login(admin)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "add_product.html")

    def test_add_product_get_non_superuser_redirects_home(self):
        user = User.objects.create_user(username="user", password="pass")
        self.client.force_login(user)
        response = self.client.get(self.url)
        self.assertRedirects(response, self.home_url)


class AddSpecsAdminAccessTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin = User.objects.create_superuser(
            username="admin",
            password="adminpass",
            email="admin@example.com",
        )
        self.user = User.objects.create_user(username="user", password="pass")
        self.product = Products.objects.create(
            name="Admin Phone",
            price=100000,
            category="Telefon",
            colors=["black"],
            image_path=["phone.jpg"],
            stock=[10],
        )
        self.url = reverse("add_specs", args=[self.product.id])
        self.home_url = reverse("home")

    def test_add_specs_get_superuser_can_access(self):
        self.client.force_login(self.admin)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "add_specs.html")

    def test_add_specs_get_non_superuser_redirects_home(self):
        self.client.force_login(self.user)
        response = self.client.get(self.url)
        self.assertRedirects(response, self.home_url)


class AllUserOrderAdminViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin = User.objects.create_superuser(
            username="admin",
            password="adminpass",
            email="admin@example.com",
        )
        self.user = User.objects.create_user(username="user", password="pass")
        self.url = reverse("all_user_order")
        self.home_url = reverse("home")

    def test_all_user_order_superuser_sees_order_list(self):
        Orders.objects.create(user=self.user, status="feldolgozás_alatt")
        Orders.objects.create(user=self.user, status="kiszállítva")

        self.client.force_login(self.admin)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "list_orders.html")
        orders_in_context = list(response.context["orders"])
        self.assertEqual(len(orders_in_context), 2)

    def test_all_user_order_non_superuser_redirects_home(self):
        self.client.force_login(self.user)
        response = self.client.get(self.url)
        self.assertRedirects(response, self.home_url)

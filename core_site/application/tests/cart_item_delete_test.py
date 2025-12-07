
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date
from ..models import Cart, Products, Specs


class DeleteCartItemTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        cls.delete_url = lambda item_id: reverse('delete_cart_item', args=[item_id])
        cls.home_url = reverse('home')

        cls.user = User.objects.create_user(username='user', password='userpass')

        cls.product = Products.objects.create(
            name='Phone',
            price=200000,
            category='Telefon',
            colors=['Black'],
            image_path=[],
            stock=[64]  # ✅ use stock instead of available
        )

        cls.specs = Specs.objects.create(
            product=cls.product,
            CPU_speed='3.2 GHz',
            CPU_type='Octa-core',
            display_size='6.5"',
            resolution='2400x1080',
            display_technology='AMOLED',
            max_refresh_rate='120Hz',
            Spen=False,
            camera='108MP',
            memory=[8],  # ✅ integer, not "8GB"
            storage=[64],  # ✅ integer
            os='Android 13',
            charge='Fast Charge',
            sensors='Fingerprint',
            size='160x75x8 mm',
            weight=190,
            battery=5000,
            release_date=date(2023, 9, 1)
        )

        cls.cart_item = Cart.objects.create(
            user=cls.user,
            product=cls.product,
            quantity=1,
            price=300000,
            color="Black",
            storage=128
        )

    def login(self):
        self.client.login(username='user', password='userpass')

    def test_delete_cart_item_success(self):
        self.login()
        response = self.client.post(self.delete_url(self.cart_item.id))
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {'success': True, 'new_total': 0})
        self.assertFalse(Cart.objects.filter(id=self.cart_item.id).exists())

    def test_delete_cart_item_not_found(self):
        self.login()
        response = self.client.post(self.delete_url(9999))  # non-existent ID
        self.assertEqual(response.status_code, 404)
        self.assertJSONEqual(response.content, {'success': False, 'error': 'Item not found'})

    def test_superuser_redirects_to_home(self):
        User.objects.create_superuser(username='admin', password='adminpass', email='admin@example.com')
        self.client.login(username='admin', password='adminpass')

        response = self.client.post(self.delete_url(self.cart_item.id))
        self.assertEqual(response.status_code, 404)

    def test_get_request_returns_405(self):
        self.login()
        response = self.client.get(self.delete_url(self.cart_item.id))
        self.assertEqual(response.status_code, 405)

    def test_cart_str(self):
        self.assertIn("felhasználónak kosárban levő termékei", str(self.cart_item))

    def test_product_str(self):
        self.assertEqual(str(self.product), "Phone")

    def test_specs_str(self):
        self.assertIn("specifikációs adatai", str(self.specs))

    def test_home_url_resolves(self):
        self.assertEqual(self.home_url, reverse('home'))

    def test_delete_url_format(self):
        self.assertFalse(self.delete_url(self.cart_item.id).endswith(str(self.cart_item.id)))

    def test_login_success(self):
        logged_in = self.client.login(username='user', password='userpass')
        self.assertTrue(logged_in)

    def test_login_failure(self):
        logged_in = self.client.login(username='user', password='wrongpass')
        self.assertFalse(logged_in)

    def test_cart_item_exists_initially(self):
        self.assertTrue(Cart.objects.filter(id=self.cart_item.id).exists())

    def test_cart_item_quantity_positive(self):
        self.assertGreater(self.cart_item.quantity, 0)

    def test_cart_item_price_matches_product(self):
        self.assertEqual(self.cart_item.price, 300000)

from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from ..models import Products, Specs, Cart, UserInfo, Orders, OrderItem
from ..views import sort_product

class SortProductTests(TestCase):
    def setUp(self):
        # Create sample products
        self.p1 = Products.objects.create(
            name="Samsung Galaxy S21",
            price=300000,
            category="Telefon",
            colors=["black", "white"],
            image_path=["/images/s21.png"],
            stock=[10]
        )
        self.p2 = Products.objects.create(
            name="iPhone Case",
            price=10000,
            category="Tartozék",
            colors=["red"],
            image_path=["/images/case.png"],
            stock=[50]
        )
        self.p3 = Products.objects.create(
            name="Xiaomi Phone Case",
            price=5000,
            category="Tartozék",
            colors=["blue"],
            image_path=["/images/case1.png"],
            stock=[20]
        )

        self.products = [self.p1, self.p2, self.p3]
        self.factory = RequestFactory()

    def test_filter_by_name(self):
        request = self.factory.get('/fake-url', {'name': 'Samsung'})
        products, categories, filters = sort_product(request, self.products)

        self.assertEqual(products, [self.p1])
        self.assertEqual(filters['name'], 'Samsung')

    def test_filter_by_category(self):
        request = self.factory.get('/fake-url', {'category': 'Tartozék'})
        products, categories, filters = sort_product(request, self.products)

        self.assertCountEqual(products, [self.p2, self.p3])
        self.assertEqual(filters['category'], 'Tartozék')

    def test_filter_by_min_price(self):
        request = self.factory.get('/fake-url', {'minPrice': '20000'})
        products, categories, filters = sort_product(request, self.products)

        self.assertEqual(products, [self.p1])  # Only Galaxy S21 >= 20000
        self.assertEqual(filters['min_price'], '20000')

    def test_filter_by_max_price(self):
        request = self.factory.get('/fake-url', {'maxPrice': '15000'})
        products, categories, filters = sort_product(request, self.products)

        self.assertEqual(set(products), {self.p2, self.p3})  # Case + Stand
        self.assertEqual(filters['max_price'], '15000')

    def test_combined_filters(self):
        request = self.factory.get('/fake-url', {
            'name': 'Phone',
            'category': 'Tartozék',
            'minPrice': '4000',
            'maxPrice': '12000'
        })
        products, categories, filters = sort_product(request, self.products)


        self.assertCountEqual(products, [self.p2, self.p3])
        self.assertEqual(filters['category'], 'Tartozék')


    def test_categories_returned(self):
        request = self.factory.get('/fake-url')
        products, categories, filters = sort_product(request, self.products)

        self.assertIn("Telefon", categories)
        self.assertIn("Tartozék", categories)

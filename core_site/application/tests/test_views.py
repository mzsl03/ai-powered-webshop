from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from ..models import Products, Specs, Cart, UserInfo, Orders, OrderItem
from unittest.mock import patch, MagicMock
import json


class ViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.password = 'tesztjelszo123'

        self.user = User.objects.create_user(
            username='tesztuser',
            email='user@test.com',
            password=self.password,
            first_name='Teszt',
            last_name='User',
            is_staff=False,
            is_superuser=False
        )
        UserInfo.objects.create(
            user=self.user,
            address='Teszt utca 1.',
            birth_date='2000-01-01',
            phone_number='06301234567'
        )

        self.superuser = User.objects.create_superuser(
            username='adminuser',
            email='admin@test.com',
            password=self.password,
            first_name='Admin',
            last_name='User'
        )

        self.phone = Products.objects.create(
            name='Teszt Telefon',
            price=100000,
            category='Telefon',
            colors=['Fekete', 'Fehér'],
            image_path=['/img/phone1.jpg']
        )
        self.accessory = Products.objects.create(
            name='Teszt Tartozék',
            price=5000,
            category='Tartozék',
            colors=['Piros'],
            image_path=['/img/acc1.jpg']
        )
        
        self.specs = Specs.objects.create(
            product=self.phone,
            CPU_speed='2.5GHz',
            CPU_type='Octuple',
            display_size='6.1 inch',
            resolution='2340x1080',
            display_technology='OLED',
            max_refresh_rate='120Hz',
            Spen=False,
            camera='12MP',
            memory=[8],
            storage=[128, 256],
            os='Android',
            charge='15W',
            sensors='Fingerprint',
            size='150x70x7.8mm',
            weight=170,
            battery=4500,
            release_date='2023-01-01' 
        )
        self.phone.stock = [10] * 4
        self.phone.save()

        self.cart_item = Cart.objects.create(
            user=self.user,
            product=self.phone,
            quantity=1,
            price=self.phone.price,
            color='Fekete',
            storage=128
        )


    def test_login_view_get(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_login_view_post_success(self):
        response = self.client.post(reverse('login'), {
            'username': self.user.username,
            'password': self.password
        }, follow=True)
        self.assertRedirects(response, reverse('home'))
        self.assertTrue(response.context['user'].is_authenticated)


    def test_login_view_post_failure(self):
        response = self.client.post(reverse('login'), {
            'username': self.user.username,
            'password': 'rosszjelszo'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
        self.assertIn('Hibás felhasználónév vagy jelszó!', response.content.decode())
    
    def test_register_view_get(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

    def test_register_view_post_success(self):
        new_user_data = {
            'first_name': 'New',
            'last_name': 'User',
            'username': 'newuser',
            'email': 'new@user.com',
            'password': self.password,
            'password_confirm': self.password,
            'address': 'New Address 10',
            'birth_date': '1995-12-31',
            'phone_number': '06309876543',
        }
        response = self.client.post(reverse('register'), new_user_data, follow=True)
        
        self.assertRedirects(response, reverse('login'))
        self.assertTrue(User.objects.filter(username='newuser').exists())
        self.assertTrue(UserInfo.objects.filter(user__username='newuser').exists())
    
    def test_logout_view(self):
        self.client.login(username=self.user.username, password=self.password)
        response = self.client.post(reverse('logout'), follow=True)
        self.assertRedirects(response, reverse('login'))
        self.assertFalse(response.context['user'].is_authenticated)

    def test_home_view_authenticated(self):
        self.client.login(username=self.user.username, password=self.password)
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertIn(self.phone, response.context['products'])

    
    def test_home_view_unauthenticated(self):
        response = self.client.get(reverse('home'))
        self.assertRedirects(response, '/?next=/home/')

    def test_home_view_filter_by_name(self):
        self.client.login(username=self.user.username, password=self.password)
        response = self.client.get(reverse('home'), {'name': 'telefon'})
        self.assertEqual(len(response.context['products']), 1)
        self.assertIn(self.phone, response.context['products'])



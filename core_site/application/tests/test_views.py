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
    
    def test_home_view_filter_by_category(self):
        self.client.login(username=self.user.username, password=self.password)
        response = self.client.get(reverse('home'), {'category': 'Tartozék'})
        self.assertEqual(len(response.context['products']), 1)
        self.assertIn(self.accessory, response.context['products'])

    def test_product_detail_phone(self):
        self.client.login(username=self.user.username, password=self.password)
        response = self.client.get(reverse('product-name', kwargs={'name': self.phone.name}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['product'], self.phone)
        self.assertEqual(response.context['specs'], self.specs)

    def test_cart_view(self):
        self.client.login(username=self.user.username, password=self.password)
        response = self.client.get(reverse('cart'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.cart_item, response.context['products'])

    def test_add_to_cart_new_item_phone(self):
        self.client.login(username=self.user.username, password=self.password)
        Cart.objects.all().delete() 

        response = self.client.post(reverse('add_to_cart', kwargs={'product_id': self.phone.id}), {
            'color': 'Fekete',
            'storage': 256
        }, follow=True)
        
        self.assertRedirects(response, reverse('cart'))
        self.assertEqual(Cart.objects.count(), 1)
        new_item = Cart.objects.first()
        self.assertEqual(new_item.storage, 256)

    def test_delete_cart_item(self):
        self.client.login(username=self.user.username, password=self.password)
        cart_item_id = self.cart_item.id
        
        response = self.client.post(reverse('delete_cart_item', kwargs={'item_id': cart_item_id}))
        
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Cart.objects.filter(id=cart_item_id).exists())


    def test_checkout_success(self):
        self.client.login(username=self.user.username, password=self.password)
        initial_cart_count = Cart.objects.count()

        response = self.client.get(reverse('checkout'), follow=True)
        
        self.assertRedirects(response, reverse('user_order')) 
        self.assertEqual(Cart.objects.count(), 0) 
        self.assertEqual(Orders.objects.count(), 1)

    def test_add_product_view_post_phone_success(self):
        self.client.login(username=self.superuser.username, password=self.password)
        product_data = {
            'name': 'Új Telefon',
            'price': 200000,
            'category': 'Telefon',
            'colors': 'Kék,Zöld',
            'image_path': '/img/newphone.jpg',
        }
        response = self.client.post(reverse('add_product'), product_data, follow=True)
        new_product = Products.objects.get(name='Új Telefon')
        self.assertRedirects(response, reverse('add_specs', kwargs={'product_id': new_product.id})) 

    def test_add_specs_view_post_success(self):
        self.client.login(username=self.superuser.username, password=self.password)
        temp_phone = Products.objects.create(
            name='Temp Phone', price=100, category='Telefon', colors=['Piros', 'Kék']
        )
        
        specs_data = {
            'CPU_speed': '2.0GHz',
            'CPU_type': 'Dual',
            'display_size': '5.0 inch',
            'resolution': '1080x720',
            'display_technology': 'LCD',
            'max_refresh_rate': '60Hz',
            'Spen': 'on',
            'camera': '8MP',
            'memory': '4',
            'storage': '64,128',
            'os': 'iOS',
            'charge': '5W',
            'sensors': 'Giro',
            'size': '140x60x10mm',
            'weight': 150,
            'battery': 3000,
            'release_date': '2022-10-10'
        }
        
        response = self.client.post(reverse('add_specs', kwargs={'product_id': temp_phone.id}), specs_data, follow=True)
        self.assertRedirects(response, reverse('home'))
        self.assertTrue(Specs.objects.filter(product=temp_phone).exists())

    def test_update_product_view_success(self):
        self.client.login(username=self.superuser.username, password=self.password)
        new_price = 110000
        
        update_data = {
            'name': self.phone.name, 
            'price': new_price,
            'category': self.phone.category,
            'colors': ','.join(self.phone.colors),
            'image_path': ','.join(self.phone.image_path)
        }
        
        response = self.client.post(reverse('update_product', kwargs={'product_id': self.phone.id}), update_data, follow=True)
        
        self.assertRedirects(response, reverse('home'))
        self.phone.refresh_from_db()
        self.assertEqual(self.phone.price, new_price)

    def test_update_specs_view_success(self):
        self.client.login(username=self.superuser.username, password=self.password)
        new_cpu_speed = '3.0GHz'
        
        specs_data = {
            'CPU_speed': new_cpu_speed,
            'CPU_type': self.specs.CPU_type,
            'display_size': self.specs.display_size,
            'resolution': self.specs.resolution,
            'display_technology': self.specs.display_technology,
            'max_refresh_rate': self.specs.max_refresh_rate,
            'Spen': self.specs.Spen,
            'camera': self.specs.camera,
            'memory': ','.join(map(str, self.specs.memory)),
            'storage': ','.join(map(str, self.specs.storage)),
            'os': self.specs.os,
            'charge': self.specs.charge,
            'sensors': self.specs.sensors,
            'size': self.specs.size,
            'weight': self.specs.weight,
            'battery': self.specs.battery,
            'release_date': self.specs.release_date
        }
        
        response = self.client.post(reverse('update_specs', kwargs={'specs_id': self.specs.id}), specs_data, follow=True)
        
        self.assertRedirects(response, reverse('home'))
        self.specs.refresh_from_db()
        self.assertEqual(self.specs.CPU_speed, new_cpu_speed)


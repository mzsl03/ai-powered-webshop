from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from application.forms.register_form import RegistrationForm
from application.models import UserInfo
import datetime


class RegisterViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.home_url = reverse('home')

        self.valid_data = {
            'first_name': 'Teszt',
            'last_name': 'Elek',
            'username': 'tesztelek',
            'email': 'teszt.elek@example.com',
            'password': 'password123',
            'password2': 'password123',
            'address': 'Budapest, Teszt utca 5.',
            'birth_date': '1990-01-01',
            'phone_number': '36701234567'
        }

    def test_successful_registration(self):
        response = self.client.post(self.register_url, self.valid_data, follow=True)

        self.assertRedirects(response, self.login_url)

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Sikeres regisztráció')
        self.assertEqual(messages[0].level_tag, 'success')

        self.assertTrue(User.objects.filter(username='tesztelek').exists())
        user = User.objects.get(username='tesztelek')

        self.assertTrue(UserInfo.objects.filter(user=user).exists())
        user_info = UserInfo.objects.get(user=user)
        self.assertEqual(user_info.address, 'Budapest, Teszt utca 5.')
        self.assertEqual(user_info.birth_date, datetime.date(1990, 1, 1))

    def test_invalid_form_data(self):
        invalid_data = self.valid_data.copy()
        invalid_data['email'] = 'rossz-email-formátum'


        response = self.client.post(self.register_url, invalid_data)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

        self.assertIn('form', response.context)
        self.assertFalse(response.context['form'].is_valid())
        self.assertIn('email', response.context['form'].errors)

        self.assertFalse(User.objects.filter(username='tesztelek').exists())

    def test_duplicate_username(self):
        User.objects.create_user(username=self.valid_data['username'], password='testpassword')

        response = self.client.post(self.register_url, self.valid_data)


        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')


        self.assertIn('form', response.context)
        self.assertIn('username', response.context['form'].errors)


        self.assertEqual(User.objects.filter(username=self.valid_data['username']).count(), 1)

    def test_get_request(self):
        response = self.client.get(self.register_url)


        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')


        self.assertIsInstance(response.context['form'], RegistrationForm)


    def test_redirect_if_authenticated(self):

        user = User.objects.create_user(username='logged_in', password='testpassword')
        self.client.force_login(user)

        response = self.client.get(self.register_url)
        self.assertRedirects(response, self.home_url)

        response_post = self.client.post(self.register_url, self.valid_data)
        self.assertRedirects(response_post, self.home_url)
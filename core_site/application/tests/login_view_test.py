from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages

class LoginViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login')
        self.home_url = reverse('home') # Feltételezett 'home' URL
        self.username = 'testuser'
        self.password = 'password123'
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_successful_login(self):
        response = self.client.post(self.login_url, {
            'username': self.username,
            'password': self.password
        }, follow=True)

        self.assertRedirects(response, self.home_url)

        self.assertTrue('_auth_user_id' in self.client.session)

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), f"Sikeresen bejelentkezett {self.username}!")
        self.assertEqual(messages[0].level_tag, 'success')


    def test_invalid_password(self):
        response = self.client.post(self.login_url, {
            'username': self.username,
            'password': 'wrongpassword'
        })

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

        self.assertIn('error', response.context)
        self.assertEqual(response.context['error'], 'Hibás felhasználónév vagy jelszó!')

        self.assertFalse('_auth_user_id' in self.client.session)


    def test_non_existent_username(self):
        response = self.client.post(self.login_url, {
            'username': 'nonexistentuser',
            'password': self.password
        })

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

        self.assertIn('error', response.context)
        self.assertEqual(response.context['error'], 'Hibás felhasználónév vagy jelszó!')


    def test_empty_fields(self):
        response_empty_username = self.client.post(self.login_url, {
            'username': '',
            'password': self.password
        })

        self.assertEqual(response_empty_username.status_code, 200)
        self.assertEqual(response_empty_username.context['error'], "Minden mező kitöltése kötelező!")

        response_empty_password = self.client.post(self.login_url, {
            'username': self.username,
            'password': ''
        })

        self.assertEqual(response_empty_password.status_code, 200)
        self.assertEqual(response_empty_password.context['error'], "Minden mező kitöltése kötelező!")


    def test_already_logged_in_user(self):
        self.client.login(username=self.username, password=self.password)

        response = self.client.get(self.login_url)

        self.assertRedirects(response, self.home_url)


    def test_get_request(self):
        response = self.client.get(self.login_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

        self.assertIn('error', response.context)
        self.assertEqual(response.context['error'], "")
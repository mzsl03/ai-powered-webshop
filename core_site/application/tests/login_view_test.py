from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from unittest.mock import patch, MagicMock

# Feltételezve, hogy a 'home' URL név létezik
# Feltételezve, hogy a login view a 'login' URL név alatt van bejegyezve

class LoginViewTest(TestCase):
    """
    Teszteli a login view viselkedését különböző forgatókönyvek esetén.
    """

    def setUp(self):
        """Beállítja a tesztkörnyezetet a tesztek futtatása előtt."""
        self.client = Client()
        self.login_url = reverse('login')
        self.home_url = reverse('home') # Feltételezett 'home' URL
        self.username = 'testuser'
        self.password = 'password123'
        self.user = User.objects.create_user(username=self.username, password=self.password)

    # 1. Teszt: Sikeres bejelentkezés
    def test_successful_login(self):
        """
        Teszteli a sikeres bejelentkezést érvényes hitelesítő adatokkal.
        """
        response = self.client.post(self.login_url, {
            'username': self.username,
            'password': self.password
        }, follow=True)

        # Ellenőrzés: Átirányítás a 'home'-ra
        self.assertRedirects(response, self.home_url)

        # Ellenőrzés: A felhasználó be van jelentkezve (az utolsó válasz a home_url)
        self.assertTrue('_auth_user_id' in self.client.session)

        # Ellenőrzés: Sikeres üzenet
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), f"Sikeresen bejelentkezett {self.username}!")
        self.assertEqual(messages[0].level_tag, 'success')


    # 2. Teszt: Helytelen jelszó
    def test_invalid_password(self):
        """
        Teszteli a bejelentkezési kísérletet helytelen jelszóval.
        """
        response = self.client.post(self.login_url, {
            'username': self.username,
            'password': 'wrongpassword'
        })

        # Ellenőrzés: A view visszatérít egy renderelt oldalt (nem átirányítás)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

        # Ellenőrzés: Hibaüzenet
        self.assertIn('error', response.context)
        self.assertEqual(response.context['error'], 'Hibás felhasználónév vagy jelszó!')

        # Ellenőrzés: A felhasználó nincs bejelentkezve
        self.assertFalse('_auth_user_id' in self.client.session)


    # 3. Teszt: Nem létező felhasználónév
    def test_non_existent_username(self):
        """
        Teszteli a bejelentkezési kísérletet nem létező felhasználónévvel.
        """
        response = self.client.post(self.login_url, {
            'username': 'nonexistentuser',
            'password': self.password
        })

        # Ellenőrzés: A view visszatérít egy renderelt oldalt (nem átirányítás)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

        # Ellenőrzés: Hibaüzenet
        self.assertIn('error', response.context)
        self.assertEqual(response.context['error'], 'Hibás felhasználónév vagy jelszó!')


    # 4. Teszt: Üres mezők
    def test_empty_fields(self):
        """
        Teszteli a bejelentkezési kísérletet üres felhasználónévvel és/vagy jelszóval.
        """
        # Üres felhasználónév, érvényes jelszó (de az authenticate sikertelen lesz)
        response_empty_username = self.client.post(self.login_url, {
            'username': '',
            'password': self.password
        })

        # Ellenőrzés: Kötelező mező üzenet
        self.assertEqual(response_empty_username.status_code, 200)
        self.assertEqual(response_empty_username.context['error'], "Minden mező kitöltése kötelező!")

        # Érvényes felhasználónév, üres jelszó
        response_empty_password = self.client.post(self.login_url, {
            'username': self.username,
            'password': ''
        })

        # Ellenőrzés: Kötelező mező üzenet
        self.assertEqual(response_empty_password.status_code, 200)
        self.assertEqual(response_empty_password.context['error'], "Minden mező kitöltése kötelező!")


    # 5. Teszt: Már bejelentkezett felhasználó
    def test_already_logged_in_user(self):
        """
        Teszteli, hogy a már bejelentkezett felhasználók a 'home' oldalra kerülnek átirányításra.
        """
        # Bejelentkezés a tesztklienssel
        self.client.login(username=self.username, password=self.password)

        # GET kérés a login view-ra
        response = self.client.get(self.login_url)

        # Ellenőrzés: Átirányítás a 'home'-ra
        self.assertRedirects(response, self.home_url)


    # 6. Teszt: GET kérés (bónusz teszt)
    def test_get_request(self):
        """
        Teszteli a kezdeti GET kérést a login oldal betöltéséhez.
        """
        response = self.client.get(self.login_url)

        # Ellenőrzés: 200 OK és a helyes sablon használata
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

        # Ellenőrzés: Nincs hibaüzenet
        self.assertIn('error', response.context)
        self.assertEqual(response.context['error'], "")
from django.test import TestCase, Client
from django.urls import reverse

class ProductMock:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value


class AIChatApiTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.api_url = reverse('ai_chat_api')

        self.mock_products = [
            ProductMock("Laptop Pro 15", 150000),
            ProductMock("Gaming Headset", 25000),
        ]
        self.expected_product_list = [
            ('Laptop Pro 15', 150000),
            ('Gaming Headset', 25000)
        ]

        self.mock_openai_reply = "Persze, szívesen ajánlom a Laptop Pro 15-öt. Ez kiváló választás a munkához. http://127.0.0.1:8000/product/Laptop%20Pro%2015/"
        self.expected_text = "Persze, szívesen ajánlom a Laptop Pro 15-öt. Ez kiváló választás a munkához."
        self.expected_link = "http://127.0.0.1:8000/product/Laptop%20Pro%2015/"

    def setup_openai_mock(self, mock_openai, reply_text):
        mock_instance = mock_openai.return_value
        mock_instance.responses.create.return_value.output_text = reply_text
        return mock_instance
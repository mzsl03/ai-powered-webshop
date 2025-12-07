from django.test import TestCase, Client
from django.urls import reverse
from unittest.mock import patch
import json

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

    @patch('application.views.OpenAI')
    @patch('application.views.Products.objects')
    def test_successful_post_request(self, MockProductsManager, MockOpenAI):
        MockProductsManager.all.return_value = self.mock_products

        self.setup_openai_mock(MockOpenAI, self.mock_openai_reply)

        response = self.client.post(
            self.api_url,
            json.dumps({"message": "Laptopot szeretnék venni."}),
            content_type="application/json"
        )

        self.assertEqual(response.status_code, 200)

        response_data = response.json()
        self.assertEqual(response_data['reply'], self.expected_text)
        self.assertEqual(response_data['link'], self.expected_link)

        MockOpenAI.return_value.responses.create.assert_called_once()
        call_args = MockOpenAI.return_value.responses.create.call_args[1]

        system_prompt = call_args['input'][0]['content']
        self.assertIn(str(self.expected_product_list), system_prompt)

        self.assertEqual(call_args['input'][-1]['content'], "Laptopot szeretnék venni.")

        session = self.client.session
        self.assertIn('chat_history', session)
        self.assertEqual(len(session['chat_history']), 2)
        self.assertEqual(session['chat_history'][1]['role'], 'assistant')
        self.assertIn(self.expected_link, session['chat_history'][1]['content'])  # link hozzáadva az előzményhez
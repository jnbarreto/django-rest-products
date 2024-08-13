import requests
from django.test import TestCase
from django.conf import settings
from ..models import Product

BASE_URL = "http://localhost:8080/api/v1"
HEADERS = { 'Authorization': 'Token b1bb35a1ce4c76b8d23cef79b02958d2d1a555ee'} #token de test

class ProductAPITests(TestCase):
    def setUp(self):
        self.client = requests.Session()
        self.products_url = f"{BASE_URL}/products/"  # Ajuste conforme necessário

    def test_list_products(self):
        response = self.client.get(self.products_url, headers=HEADERS)
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertIn('results', response_data)
        self.assertIsInstance(response_data['results'], list)


    def test_create_product(self):
        data = {
            'name': 'Test Product',
            'value': 19.99,
            'description': 'A description of the test product',
        }
        response = self.client.post(self.products_url, headers=HEADERS, json=data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()['name'], 'Test Product')

    def test_retrieve_product(self):
        data = {
            'name': 'Test Product',
            'value': 19.99,
            'description': 'A description of the test product',
        }
        response = self.client.post(self.products_url, json=data, headers=HEADERS)
        product_id = response.json()['id']

        product_url = f"{BASE_URL}/products/{product_id}/"
        response = self.client.get(product_url, headers=HEADERS)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['name'], 'Test Product')

    def test_update_product(self):
        data = {
            'name': 'Test Product',
            'value': 19.99,
            'description': 'A description of the test product',
        }
        response = self.client.post(self.products_url, json=data, headers=HEADERS)
        product_id = response.json()['id']

        update_data = {
            'name': 'Updated Product',
            'value': 29.99,
            'description': 'Updated description',
        }
        product_url = f"{BASE_URL}/products/{product_id}/"
        response = self.client.put(product_url, json=update_data, headers=HEADERS)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['name'], 'Updated Product')

    def test_delete_product(self):
        data = {
            'name': 'Test Product',
            'value': 19.99,
            'description': 'A description of the test product',
        }
        response = self.client.post(self.products_url, json=data, headers=HEADERS)
        product_id = response.json()['id']

        product_url = f"{BASE_URL}/products/{product_id}/"
        response = self.client.delete(product_url, headers=HEADERS)
        self.assertEqual(response.status_code, 204)

        response = self.client.get(product_url, headers=HEADERS)
        self.assertEqual(response.status_code, 404)

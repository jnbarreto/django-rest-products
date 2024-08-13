from django.test import TestCase
from ..models import User
from rest_framework.authtoken.models import Token
import requests

BASE_URL = "http://localhost:8080/api/v1/auth"
HEADERS = { 'Authorization': 'Token b1bb35a1ce4c76b8d23cef79b02958d2d1a555ee'} #token de test

class UserTests(TestCase):

    def setUp(self):
        self.client = requests.Session()
        self.register_url = f"{BASE_URL}/registration/"
        self.sign_in_url = f"{BASE_URL}/sign-in/"
        self.sign_out_url = f"{BASE_URL}/sign-out/"

    def test_registration_api_view(self):
        data = {
            'username': 'newuser',
            'first_name': 'user',
            'last_name': 'user last',
            'email': 'user@email.com',
            'cpf': '687.397.960-00', #cpf gerado no 4dev
            'password': 'newpassword',
            'confirm_password':'newpassword'
        }
        response = self.client.post(self.register_url, headers=HEADERS, json=data)
        print(response.status_code)
        self.assertEqual(response.status_code, 201)
        self.assertIn('username', response.json())
        self.assertEqual(response.json()['username'], 'newuser')

    def test_sign_in_view(self):
        data = {
            'username': 'newuser',
            'password': 'newpassword'
        }
        response = self.client.post(self.sign_in_url, headers=HEADERS, json=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('token', response.json())


from rest_framework.test import APITestCase, URLPatternsTestCase
from django.contrib.auth.models import User
import json

class AccountTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='Atikunchik', password='Atikun00')

    def test_login(self):
        data = {'username': 'Atikunchik', 'password': 'Atikun00'}
        response = self.client.post('/login/', data)
        self.assertEqual(response.status_code, 200)

    def test_get_token(self):
        data = {'username': 'Atikunchik', 'password': 'Atikun00'}
        response = self.client.post('/login/', data)
        data = json.loads(response.content.decode('utf-8'))
        token = data.get('token')
        if token is not None:
            self.assertEqual(response.status_code, 200)

    def test_not_login(self):
        data = {'username': 'tikunchik', 'password': 'Atikun00'}
        response = self.client.post('/login/', data)
        self.assertEqual(response.status_code, 400)

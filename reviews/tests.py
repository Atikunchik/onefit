from django.urls import include, reverse
from rest_framework import status
from django.test import TestCase, Client
from rest_framework.test import URLPatternsTestCase
from django.contrib.auth.models import User
from .models import Review, Company
from rest_framework.authtoken.models import Token
import json


class ReviewsTest(TestCase):

    def setUp(self):
        self.user1 = User.objects.create_user(username='Atikunchik', password='Atikun00')
        self.user2 = User.objects.create_user(username='Nurbergen', password='Khina000')
        self.company1 = Company.objects.create(name='Feetbook', description='feetface')
        self.company2 = Company.objects.create(name='facepaper', description='bookface')
        self.review1 = Review.objects.create(title='R', rating=3, description='qwe', company=self.company1, user=self.user1)
        self.review2 = Review.objects.create(title='W', rating=4, description='ewq', company=self.company2, user=self.user2)

    def test_good_add_review(self):
        data = {'username': 'Atikunchik', 'password': 'Atikun00'}
        response = self.client.post('/login/', data)
        data = json.loads(response.content.decode('utf-8'))
        token = data.get('token')
        headers = {
                'HTTP_AUTHORIZATION': token
        }
        review_data = {'title': 'Feet is not face', 'rating': 5, 'description': 'amazing feets', 'company_id': '1'}
        print(token, "HERE TOKEN")
        response = self.client.post('/reviews/add_review/', review_data, **headers)
        self.assertEqual(response.status_code, 200)

    def test_review_list(self):
        data = {'username': 'Atikunchik', 'password': 'Atikun00'}
        response = self.client.post('/login/', data)
        data = json.loads(response.content.decode('utf-8'))
        token = data.get('token')
        user = User.objects.filter(auth_token=token).first()
        headers = {
            'HTTP_AUTHORIZATION': token
        }
        response = self.client.post('/reviews/', {}, **headers)
        data = json.loads(response.content.decode('utf-8'))
        print(data)
        print(user)
        print(data.get('latest_review_list'))
        reviews_list = data.get('latest_review_list')
        for i in reviews_list:
            print(user is User.objects.filter(id=i.get('user')).first())
            review = i.full()
            author = review.get('user')
            if author != user.id:
                self.assertEqual(response.status_code, 400)
        self.assertEqual(response.status_code, 200)

    def test_del(self):
        data = {'username': 'Atikunchik', 'password': 'Atikun00'}
        response = self.client.post('/login/', data)
        data = json.loads(response.content.decode('utf-8'))
        token = data.get('token')
        user = User.objects.filter(auth_token=token).first()
        headers = {
            'HTTP_AUTHORIZATION': token
        }
        response = self.client.post('/reviews/1/', {}, **headers)
        print(User.objects.all())
        self.assertEqual(response.status_code, 400)



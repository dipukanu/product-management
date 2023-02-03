from rest_framework.test import (
    APITestCase,
    APIClient,
)
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework import status


CREATE_USER_URL = reverse('user:create-user')
TOKEN_URL = reverse('token_obtain_pair')


def create_user(**params):
    """Create and return user"""
    return get_user_model().objects.create_user(**params)


class PublicUserApiTests(APITestCase):
    """Test the public feature of API"""

    def setUp(self):
        self.client = APIClient()

    def create_user_success(self):
        payload = {
            'email': 'test1@example.com',
            'password': 'pass123df',
            'name': 'Create User Test',
        }
        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(email=payload['email'])
        self.assertTrue(user.check_password(payload['password']))
        self.assertNotIn('password', res.data)

    def test_user_with_email_exists_error(self):
        payload = {
            'email': 'test1@example.com',
            'password': 'pass123df',
            'name': 'Exist Email Test',
        }
        create_user(**payload)
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

        user_exist = get_user_model().objects.filter(
            email=payload['email']
        ).exists()

        self.assertTrue(user_exist)

    """Test generate token for user with valid credentials"""

    def test_create_token_for_user(self):
        user_details = {
            'email': 'testtoken@gmail.com',
            'password': 'Test1234mm',
        }
        create_user(**user_details)

        payload = {
            'email': user_details['email'],
            'password': user_details['password'],
        }

        res = self.client.post(TOKEN_URL, payload)

        self.assertIn('access', res.data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_not_create_token_without_password(self):
        payload = {'email': 'test@gmail.com', 'password': ''}
        res = self.client.post(TOKEN_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

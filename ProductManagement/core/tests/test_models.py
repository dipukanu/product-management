from django.test import TestCase

from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_mail(self):
        email = 'test@gmail.com'
        password = 'PAss1234'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_create_superuser(self):
        email = 'test@gmail.com'
        user = get_user_model().objects.create_superuser(email, 'dfjdhfhdf')
        self.assertTrue(user.is_superuser)

from decimal import Decimal

from django.contrib.auth import get_user_model

from django.urls import reverse

from rest_framework import status

from rest_framework.test import APITestCase, APIClient

from core.models import (
    Product,
    ProductCategory,
    ProductImage,
)

from product.serializers import (
    ProductCategorySerializer,
    ProductSerializer,
    ProductImageSerializer
)

CATEGORY_URL = reverse('product:create-category')
CATEGORY_DETIAL = reverse('product:category-details')


def create_user(**params):
    """Create and return user"""
    return get_user_model().objects.create_user(**params)


def create_category(**params):
    default = {
        'name': 'TV'
    }
    default.update(params)
    category = ProductCategory.objects.create(**default)
    return category


class PrivateAPITest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = create_user(
            email='testprivate@gmail.com',
            password='testpass357',
            name='Private API',
        )
        self.client.force_authenticate(user=self.user)
    """Test create product category"""

    def test_create_product_category(self):
        payload = {
            'name': 'FlipFlop'
        }
        res = self.client.post(CATEGORY_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_product_category_details(self):
        create_category()
        res = self.client.get(CATEGORY_DETIAL)

        categories = ProductCategory.objects.all()
        serializer = ProductCategorySerializer(categories, many=True)

        self.assertEqual(res.data, serializer.data)
        self.assertTrue(serializer.data)

from decimal import Decimal

from django.contrib.auth import get_user_model

from django.core.files.uploadedfile import SimpleUploadedFile

from django.test import TestCase

from core import models


class ModelTests(TestCase):

    def test_product_category(self):
        category = models.ProductCategory.objects.create(
            name='Mobile'
        )
        self.assertEqual(category.name, 'Mobile')

    def test_product(self):
        user = get_user_model().objects.create_user(
            'test@gmail.com',
            'pass1230',
        )
        product = models.Product.objects.create(
            user=user,
            product_name='Redmi Note 10 pro max',
            description='Bla Bla',
            price=Decimal('400.00'),
        )
        product.save()
        category1 = product.category.create(name='Mobile')
        category1.save()
        self.assertEqual(str(product), product.product_name)
        self.assertEqual(category1.name, "Mobile")

    def test_product_image(self):
        user = get_user_model().objects.create_user(
            'test@gmail.com',
            'pass1230',
        )
        product = models.Product.objects.create(
            user=user,
            product_name='Redmi Note 10 pro max',
            description='Bla Bla',
            price=Decimal('400.00'),
        )
        product.save()
        image = models.ProductImage.objects.create(
            product=product,
            image=SimpleUploadedFile(
                name='test_image.jpg', content=b"Content/ path", content_type='image/jpeg')
        )
        self.assertEqual(models.ProductImage.objects.count(), 1)
        self.assertTrue(image.image)

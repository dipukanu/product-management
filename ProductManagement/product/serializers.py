from rest_framework import serializers

from core.models import (
    ProductCategory,
    Product,
    ProductImage,
)


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['id', 'name']


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'product', 'image']


class ProductSerializer(serializers.ModelSerializer):

    images = ProductImageSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(allow_empty_file=False, use_url=False),
        write_only=True
    )
    category = ProductCategorySerializer(many=True)

    class Meta:
        model = Product
        fields = ['id', 'user', 'product_name', 'description',
                  'price', 'images', 'uploaded_images', 'category', 'slug']

    def create(self, validated_data):
        uploaded_images = validated_data.pop("uploaded_images")
        product = Product.objects.create(**validated_data)

        for image in uploaded_images:
            NewProImg = ProductImage.objects.create(
                product=product, image=image)

        return product

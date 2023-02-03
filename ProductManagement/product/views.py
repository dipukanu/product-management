from rest_framework import status, permissions

from rest_framework.views import APIView

from rest_framework.response import Response

from rest_framework.parsers import (
    MultiPartParser,
    FormParser,
)

from django.shortcuts import get_object_or_404


from core.models import (
    ProductCategory,
    Product,
    ProductImage
)

from product.serializers import (
    ProductCategorySerializer,
    ProductSerializer,
    ProductImageSerializer,

)


class CreateCategoryView(APIView):
    serializer_class = ProductCategorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = ProductCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class ListCategoryView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        category = ProductCategory.objects.all()
        serializer = ProductCategorySerializer(category, many=True)

        return Response(serializer.data)


class ManageCategoryView(APIView):
    serializer_class = ProductCategorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        category = get_object_or_404(ProductCategory, pk=pk)
        serializer = ProductCategorySerializer(category)
        return Response(serializer.data)

    def put(self, request, pk):
        category = get_object_or_404(ProductCategory, pk=pk)
        serializer = ProductCategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        category = get_object_or_404(ProductCategory, pk=pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CreateProductView(APIView):
    serializer_class = ProductSerializer
    parser_class = (MultiPartParser, FormParser)
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class ListProductView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)

        return Response(serializer.data)


class ManageProductView(APIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, slug):
        product = get_object_or_404(Product, slug=slug)
        serializer = ProductSerializer(product)

        return Response(serializer.data)

    def put(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(product, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_304_NOT_MODIFIED)

    def delete(self, pk):
        product = get_object_or_404(Product, pk=pk)
        product.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class CreateProductImageView(APIView):
    serializer_class = ProductImageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = ProductImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class ListProductImageView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        images = ProductImage.objects.all()
        serializer = ProductImageSerializer(images, many=True)

        return Response(serializer.data)


class ManageProductImageView(APIView):
    serializer_class = ProductImageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        image = get_object_or_404(ProductImage, pk=pk)
        serializer = ProductImageSerializer(image)

        return Response(serializer.data)

    def put(self, request, pk):
        image = get_object_or_404(ProductImage, pk=pk)
        serializer = ProductImageSerializer(image, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_304_NOT_MODIFIED)

    def delete(self, pk):
        image = get_object_or_404(ProductImage, pk=pk)
        image.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

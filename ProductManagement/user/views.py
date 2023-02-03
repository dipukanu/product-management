from rest_framework.views import APIView

from rest_framework.response import Response

from rest_framework import status, permissions

from django.shortcuts import get_object_or_404

from core.models import User

from user.serializers import (
    UserSerializer,
    UserPostSerializer,
)


class CreateUserView(APIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class ListUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        query = User.objects.all()
        serializer = UserSerializer(query, many=True)
        return Response(serializer.data)


class ManageUserView(APIView):
    serializer_class = UserPostSerializer
    permission_classes = [permissions.IsAuthenticated]

    """Retrieve"""

    def get(self, request, id):
        query = get_object_or_404(User, id=id)
        serializer = UserSerializer(query)
        return Response(serializer.data)

    """Update"""

    def put(self, request, id):
        query = get_object_or_404(User, id=id)
        serializer = UserPostSerializer(query, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_304_NOT_MODIFIED)

    """Delete"""

    def delete(self, request, id):
        query = get_object_or_404(User, id=id)
        query.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

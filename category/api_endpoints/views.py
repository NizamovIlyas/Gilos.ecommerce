# category/api_endpoints/views.py

from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from category.models import Category
from .serializer import CategorySerializer


class CategoryListCreateAPIView(ListCreateAPIView):
    """
    GET: List all categories
    POST: Create a new category
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """
    GET: Retrieve a specific category
    PUT: Update a category
    DELETE: Delete a category
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

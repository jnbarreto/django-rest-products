from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer


class ProductsAPIView(generics.ListCreateAPIView):
    """
    API Product Bnex - Create and Get
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API Product Bnex - Update and Delete
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

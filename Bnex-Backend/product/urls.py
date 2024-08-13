from django.urls import path
from .views import ProductAPIView, ProductsAPIView

urlpatterns = [
    path('products/', ProductsAPIView.as_view(), name='products'),
    path('products/<int:pk>/', ProductAPIView.as_view(), name='product'),
]

from django.urls import path
from .views import ProductAPIView, ProductDetailAPIView

urlpatterns = [
    # Handles both GET (list) and POST (create)
    path('products/', ProductAPIView.as_view(), name='products'),
    path('products/<int:id>/', ProductDetailAPIView.as_view(),
         name='product-detail'),  # Handles GET for specific product
]

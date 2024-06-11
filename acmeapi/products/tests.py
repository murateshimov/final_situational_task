from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Product


class ProductTests(APITestCase):
    def test_create_product(self):
        """
        Ensure we can create a new product object.
        """
        url = reverse('create-product')
        data = {'name': 'New Product', 'description': 'Detailed description',
                'price': 19.99, 'category': 'Electronics'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(Product.objects.get().name, 'New Product')


def test_retrieve_product(self):
    """
    Test retrieving a product after creating it.
    """
    create_url = reverse('create-product')
    def detail_url(pk): return reverse('detail-product', kwargs={'id': pk})
    data = {'name': 'Integration Product', 'description': 'Test',
            'price': 20.00, 'category': 'Test Category'}

    create_response = self.client.post(create_url, data, format='json')
    product_id = create_response.data['id']

    retrieve_response = self.client.get(detail_url(product_id))
    self.assertEqual(retrieve_response.status_code, status.HTTP_200_OK)
    self.assertEqual(retrieve_response.data['name'], data['name'])

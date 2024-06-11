import requests

# Base URL of your Django server
BASE_URL = 'http://127.0.0.1:8000/api/'


def create_product():
    url = f"{BASE_URL}products/"
    product_data = {
        'name': 'New Product',
        'description': 'A product description here.',
        'price': 29.99,
        'category': 'Electronics'
    }
    response = requests.post(url, json=product_data)
    print("Create Product Status:", response.status_code)
    try:
        print("Response:", response.json())
    except requests.exceptions.JSONDecodeError:
        print("Response not in JSON format")
    return response


def get_products():
    url = f"{BASE_URL}products/"
    response = requests.get(url)
    print("Get Products Status:", response.status_code)
    print("Response:", response.json())


def get_product_by_id(product_id):
    url = f"{BASE_URL}products/{product_id}/"
    response = requests.get(url)
    print("Get Product Details Status:", response.status_code)
    print("Response:", response.json())


if __name__ == "__main__":
    # Test creating a product
    product = create_product()

    # Test getting list of products
    get_products()

    # Test getting a specific product by ID
    if 'id' in product:
        get_product_by_id(product['id'])

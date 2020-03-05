from django.test import TestCase
from .models import Product, Category

# Create your tests here.

class TestProduct(TestCase):
    """Testing the Product model"""
    def test_title(self):
        title_testing = Product(title = "Test Title")
        self.assertEqual(str(title_testing), "Test Title")
        self.assertNotEqual(str(title_testing), "something else")

class TestCategory(TestCase):
    """Testing the Category model"""
    def test_category(self):
        cat_name = Category(category_name = "Test Category Name")
        self.assertEqual(str(cat_name), "Test Category Name")
        self.assertNotEqual(str(cat_name), "something else")
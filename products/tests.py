from django.test import TestCase
from .models import Product, Category

# Create your tests here.

class TestProduct(TestCase):

    def test_title(self):
        title_testing = Product(title = "Test Title")
        self.assertEqual(str(title_testing), "Test Title")
        self.assertNotEqual(str(title_testing), "something else")

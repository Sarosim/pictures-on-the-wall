from django.test import TestCase
from .models import Product, Category

# Create your tests here.

class TestProduct(TestCase):
    def test_title(self):
        title_testing = Product(title = "Test Title")
        self.assertEqual(str(title_testing), "Test Title")
        self.assertNotEqual(str(title_testing), "something else")

    """ def test_repro_fee(self):
        repro_fee_testing = Product(base_repro_fee = 9.99)
        self.assertEqual(repro_fee_testing = 9.99)
        self.assertNotEqual(repro_fee_testing = 10) """
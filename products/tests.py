from django.test import TestCase
from .models import Product, Category, Badge, Technologies, Rating, Artist, Size, Format

# Create your tests here.

class TestArtist(TestCase):
    """ Testing the Badge model """
    def test_artist(self):
        artist_name = Artist(display_name = "Test name")
        self.assertEqual(str(artist_name), "Test name")

class TestTechnologies(TestCase):
    """ Testing the technologies model """
    def test_technologies(self):
        techn_name = Technologies(technology_name = "Test Technology")
        self.assertEqual(str(techn_name), "Test Technology")

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

class TestBadge(TestCase):
    """Testing the Badge model"""
    def test_badge(self):
        test_badge_name = Badge(badge_name = "Test Badge Name")
        self.assertEqual(str(test_badge_name), "Test Badge Name")
        self.assertNotEqual(str(test_badge_name), "something else")

class TestSize(TestCase):
    """Testing the Size model"""
    def test_size(self):
        test_size_name = Size(size_name = "Test Size Name")
        self.assertEqual(str(test_size_name), "Test Size Name")
        self.assertNotEqual(str(test_size_name), "something else")

class TestFormat(TestCase):
    """Testing the Format model"""
    def test_format(self):
        test_format_name = Format(format_name = "Test Format Name")
        self.assertEqual(str(test_format_name), "Test Format Name")
        self.assertNotEqual(str(test_format_name), "something else")
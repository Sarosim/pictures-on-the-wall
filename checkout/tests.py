from django.test import TestCase
from .models import Order, OrderLineItem
from django.utils import timezone

# Create your tests here.

class TestOrder(TestCase):
    """ Testing the Order model """
    def test_order(self):
        string = Order(id = "1", date = "2020-03-20 18:06:34.021189+00:00", first_name = "Test name", last_name = "Test last")
        self.assertEqual(str(string), "1-2020-03-20 18:06:34.021189+00:00-Test name-Test last")


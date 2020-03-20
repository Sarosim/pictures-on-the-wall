from django.db import models
from products.models import Product

# Create your models here.
class Order(models.Model):
    """ Model for the order when a user wants to checkout """
    first_name = models.CharField(max_length=32, blank=False)
    last_name = models.CharField(max_length=32, blank=False)
    phone_number = models.CharField(max_length=16, blank=False)
    country = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=20, blank=True)
    town_or_city = models.CharField(max_length=40, blank=False)
    address_line1 = models.CharField(max_length=40, blank=False)
    address_line2 = models.CharField(max_length=40, blank=False)
    date = models.DateField()

    def __str__(self):
        return "{0}-{1}-{2}-{3}".format(self.id, self.date, self.first_name, self.last_name)


class OrderLineItem(models.Model):
    """ Model for storing each item of the Order """
    order = models.ForeignKey(Order, null=False)
    product = models.ForeignKey(Product, null=False)
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return "{0} {1} @ {2}".format(self.quantity, self.product.title, self.product.base_repro_fee)

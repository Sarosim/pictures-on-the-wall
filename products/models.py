from django.db import models

# Create your models here.

class Category(models.Model):
    """Artwork (product) categories """
    category_name = models.CharField(max_length=32, default='other')
    category_description = models.TextField()

    def __str__(self):
        return self.category_name

class Product(models.Model):
    """The Product database, including the artworks """
    title = models.CharField(max_length=32, default='')
    description = models.TextField()
    base_repro_fee = models.DecimalField(max_digits=3, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


from django.db import models

# Create your models here.


class Category(models.Model):
    """Artwork (product) categories model """
    category_name = models.CharField(max_length=32, default='')
    category_description = models.TextField()

    def __str__(self):
        return self.category_name


class Badge(models.Model):
    """ Badges for Artists (eg. hobby, advanced, master, pro...) """
    badge_name = models.CharField(max_length=16)
    badge_logo = models.ImageField(upload_to='images')

    def __str__(self):
        return self.badge_name


class Artist(models.Model):
    """ Model for the Artists uploading their artwork to the site """
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    display_name = models.CharField(max_length=16)
    avatar = models.ImageField(upload_to='images')
    badge = models.ForeignKey(Badge, on_delete=models.CASCADE)
    address = models.CharField(max_length=64, default='')
    wants_marketing = models.BooleanField(default=True)
    wants_newsletter = models.BooleanField(default=True)

    def __str__(self):
        return self.display_name


class Technologies(models.Model):
    """ Model for valiable printing technologies. Each artwork is assigned to all relevant print technologies"""
    technology_name = models.CharField(max_length=32)
    technology_description = models.TextField

    def __str__(self):
        return self.technology_name


class Product(models.Model):
    """The Artwork (Product) model, contains all the artworks """
    title = models.CharField(max_length=32, default='')
    description = models.TextField()
    base_repro_fee = models.DecimalField(max_digits=3, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default='other')
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, default='')
    max_print_size = models.CharField(max_length=16, default='')
    available_technologies = models.ManyToManyField(Technologies)
    num_of_orders = models.IntegerField(default=0)
    num_of_views = models.IntegerField(default=0)
    date_uploaded = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Rating(models.Model):
    """ Products ratings: """
    product = models.ForeignKey(Product)
    rating = models.IntegerField()
    #userid (of the rater to prevent double rating) --- TO BE ADDED LATER

    def __str__(self):
        return self.rating
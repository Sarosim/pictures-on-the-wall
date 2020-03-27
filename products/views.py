from django.shortcuts import render
from .models import Product, Category, Hashtag, Rating

# Create your views here.

def all_products(request):
    """ The view rendering a page with all products listed """
    all_the_products = Product.objects.all()
    return render(request, "products.html", {"products": all_the_products})

def product_details(request, id):
    """ The view rendering the page for one selected product and all of its details """
    selected_product = Product.objects.get(pk = id)
    # filtering the hashtags associated with the selected product - excluding duplicates:
    hashtags = Hashtag.objects.filter(product = selected_product).distinct()
    # filtering all the relevant ratings from the Rating model:
    ratings = Rating.objects.filter(product = selected_product)
    ratings_total = 0
    ratings_count = 0
    if ratings:
        for rating in ratings:
            ratings_total += rating.rating
            ratings_count += 1
        ratings_average = ratings_total / ratings_count
    else:
        ratings_average = 0
    ratings_percent = round(ratings_average * 20)
    ratings_data = {
        "ratings_average": ratings_average,
        "ratings_percent": ratings_percent,
        "ratings_count": ratings_count
    }
    pass_to_template = {
        "selected_prod": selected_product,
        "hashtags": hashtags,
        "ratings_data": ratings_data
    }
    return render(request, "product_details.html", {"pass_to_template": pass_to_template})
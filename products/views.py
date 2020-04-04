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
    # filtering the hashtags associated with the selected product:
    hashtags = Hashtag.objects.filter(product = selected_product)
    print(f"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxwwwwwwwwwwwwwwwww**********selected_product : {hashtags}")
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


def filtered_products(request, filter_group, filter_name):
    """ The view rendering a page for all products (Artwork) filtered by a user selected criteria """
    
    # setting the values for the variables for quick testing before actual links properly set on page
    filter_group = 'room'
    filter_name = 'bathroom'
    
    #constructing kwargs for the filter
    if filter_group == 'hashtag':
        filter_subgroup = 'hashtag'
    else:
        filter_subgroup = filter_group + '_name'
    print(f"************************************************The function was called and the arguments are: -filter_name: {filter_name};  -filter_group: {filter_group}")
    filter_kwargs = filter_group + '__' + filter_subgroup + '__' + 'iexact'

    # the actual filtering
    filtered_products = Product.objects.filter(**{ filter_kwargs: filter_name })

    print(filtered_products)
    return render(request, "products.html", {"products": filtered_products})


def file_upload(request):
    """ The view rendering the page that explains how to become a contributor
    and upload an image, as well we the form for file upload"""
    return render(request, 'upload.html')
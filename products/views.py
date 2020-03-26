from django.shortcuts import render
from .models import Product, Category, Hashtag

# Create your views here.

def all_products(request):
    """ The view rendering a page with all products listed """
    all_the_products = Product.objects.all()
    return render(request, "products.html", {"products": all_the_products})

def product_details(request, id):
    """ The view rendering the page for one selected product and all of its details """
    selected_product = Product.objects.get(pk = id)
    print("XXXXXXXXXXXXXXXXXXX sel_prod: {}".format(selected_product))
    hashtags = Hashtag.objects.filter(product = selected_product).distinct()
    for hashtag in hashtags:
        print("XXXXXXXXXXXXXXXXXXX Hash-tags: {}".format(hashtag.hashtag))
    pass_to_template = [
        selected_product,
        hashtags
    ]
    print("YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY pass_to_templ.: {}!".format(pass_to_template[1]))
    return render(
        request, 
        "product_details.html",
        {"pass_to_template": pass_to_template}
        )
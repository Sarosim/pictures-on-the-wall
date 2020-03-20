from django.shortcuts import render
from .models import Product, Category

# Create your views here.

def all_products(request):
    """ The view rendering a page with all products listed """
    all_the_products = Product.objects.all()
    return render(request, "products.html", {"products": all_the_products})

def product_details(request):
    """ The view rendering the page for one selected product and all of its details """
    selected_product = Product.objests.get(pk = id)
    return render(request, "product_details.html", {"selected_product": selected_product})
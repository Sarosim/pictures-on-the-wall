from django.shortcuts import render
from .models import Product, Category

# Create your views here.

def all_products(request):
    """ The view rendering a page with all products listed """
    all_the_products = Product.objects.all()
    print("ez a nyomtat", all_the_products)
    return render(request, "products.html", {"products": all_the_products})
from django.shortcuts import render
from products.models import Product, Category

# Create your views here.
def search_by_title(request):
    """ Search amongst the Artworks (products) by their title """
    products = Product.objects.filter(title__icontains=request.GET['search'])

    return render(request, 'products.html', {"products": products})
from django.shortcuts import render
from products.models import Product, Category

# Create your views here.
def search_by_title(request):
    """ Search amongst the Artworks (products) by their title """
    products_by_title = Product.objects.filter(title__icontains=request.GET['search'])
    print(request.GET['search'])
    products_by_category = Product.objects.filter(category__category_name__icontains=request.GET['search'])
    products = products_by_title | products_by_category
    products_by_hashtag = Product.objects.filter(hashtag__hashtag__icontains=request.GET['search'])
    products = products | products_by_hashtag
    return render(request, 'products.html', {"products": products})
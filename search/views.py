from django.shortcuts import render, redirect, reverse
from products.models import Product, Category
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.contrib import messages

def validate_chars(string):
    """ Vaildate whether string contains non-alphnumeric characters """
    for char in string:
        if not char.isalnum():
            raise ValidationError(
                _('%(string)s contains special character, please use only alphanumerics!'),
                params={'string': string},
            )
        return

def search_by_title(request):
    """ Search amongst the Artworks (products) by their title """
    print(f"the search term from the GET: {request.GET['search']}")
    try:
        validate_chars(request.GET['search'])
    except:
        messages.error(request, 'Your search contains special character, please use only alphanumerics!')
        go_back_to = request.GET.get('go-back-to', '/')
        if go_back_to == "/search/":
            go_back_to = '/home'
        print(f"this is the url from the GET: {go_back_to}")
        return redirect(go_back_to)
    products_by_title = Product.objects.filter(title__icontains=request.GET['search'])
    
    products_by_category = Product.objects.filter(category__category_name__icontains=request.GET['search'])
    products = products_by_title | products_by_category
    products_by_hashtag = Product.objects.filter(hashtag__hashtag__icontains=request.GET['search'])
    products = products | products_by_hashtag
    
    return render(request, 'products.html', {"products": products})
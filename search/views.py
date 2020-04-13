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
    """ Search amongst the Artworks (products) by their title, \n
    it also returns products with the search term in their associated category
    or hashtags"""
    # validating the search term for special characters
    try:
        validate_chars(request.GET['search'])
    except:
        messages.error(request, 'Your search contains special character, please use only alphanumerics!')
        # getting the origin of the request from the hidden input in the form:
        go_back_to = request.GET.get('go-back-to', '/')
        # if the origin was the search page itself, we redirect to 'home' 
        if go_back_to == "/search/":
            go_back_to = '/home'
        return redirect(go_back_to)
    # filtering by title:
    products_by_title = Product.objects.filter(title__icontains=request.GET['search'])
    # then filtering by category:
    products_by_category = Product.objects.filter(category__category_name__icontains=request.GET['search'])
    # Combining the two QueryStes together
    products = products_by_title | products_by_category
    # then filtering by hashtags
    products_by_hashtag = Product.objects.filter(hashtag__hashtag__icontains=request.GET['search'])
    # and adding the hashatg QuerySet to the combined one:
    products = products | products_by_hashtag
    
    return render(request, 'products.html', {"products": products})
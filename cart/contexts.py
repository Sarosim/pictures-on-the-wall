from django.shortcuts import get_object_or_404
from products.models import Product

def cart_contents(request):
    """ Ensuring the cart contents are available for every page to be rendered """
    
    cart = request.session.get('cart', {})
    """ A cart requesting a session with the existing cart if there is one, or a blank dictionary, if there's not. """
    
    cart_items = []
    total = 0
    product_count = 0
    
    for id, quantity in cart.items():
        product = get_object_or_404(Product, pk=id)
        total += quantity * product.base_repro_fee
        product_count += quantity
        cart_items.append({'id': id, 'quantity': quantity, 'product': product})
    return {'cart_items': cart_items, 'total': total, 'product_count': product_count}
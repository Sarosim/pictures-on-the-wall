from django.shortcuts import get_object_or_404
from products.models import Product, Size, Technology

def cart_contents(request):
    """ Ensuring the cart contents are available for every page to be rendered """
    
    cart = request.session.get('cart', {})
    """ A cart requesting a session with the existing cart if there is one, or a blank dictionary, if there's not. """

    cart_items = []
    total = 0
    product_count = 0
    cart_ids = []
    
    for id, details in cart.items():
        product = get_object_or_404(Product, pk=id)
        qty = details['quantity']
        product_count += qty
        size = details['size']
        technology = details['technology']
        unit_price = details['unit_price']
        total += qty * unit_price

        cart_items.append({
            'id': id,
            'quantity': qty,
            'product': product,
            'size': size,
            'technology': technology,
            'unit_price': unit_price,
        })


    return {'cart_items': cart_items, 'total': total, 'product_count': product_count}
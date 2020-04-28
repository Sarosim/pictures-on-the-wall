from django.shortcuts import get_object_or_404
from products.models import Product, Size, Technology

def cart_contents(request):
    """ Ensuring the cart contents are available for every page to be rendered """
    
    cart = request.session.get('cart', {})
    """ A cart requesting a session with the existing cart if there is one, or a blank dictionary, if there's not. """
    # size_session = request.session.get('size_session', {})
    

    cart_items = []
    total = 0
    product_count = 0
    
    for id, details in cart.items():
        product = get_object_or_404(Product, pk=id)
        total += details['quantity'] * product.base_repro_fee
        product_count += details['quantity']
        size = details['size']

        # print("SIZES", size)
        # current_technology = product.available_technologies
        # print("CURRENT TECH", current_technology)
        cart_items.append({'id': id, 'quantity': details['quantity'], 'product': product, 'size': details['size'],})

    # cart_item_sizes = []

    # for id, size in size_session.items():
    #     product = get_object_or_404(Product, pk=id)
    #     print("SIZE: ", size)
    #     cart_item_sizes.append({'id': id, 'size': size})

    return {'cart_items': cart_items, 'total': total, 'product_count': product_count}
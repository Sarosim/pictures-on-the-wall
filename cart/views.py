from django.shortcuts import render, redirect, reverse, get_object_or_404
from products.models import Product, Size
import math

# Create your views here.

def view_cart(request):
    """ Rendering the shopping cart contents page """
    return render(request, "cart.html")


def add_to_cart(request, id):
    """ Adds the product to the cart and redirects to the page.
    (no quantity is obtained, as 99.99% of the customers will buy only one copy of the artwork)"""

    cart = request.session.get('cart', {})

    product = get_object_or_404(Product, pk=id)
    
    if id in cart:
        # If the product is in the cart already, it increases the quantity 
        cart[id]['quantity'] = int(cart[id]['quantity']) + 1      
    else:
        # If it's not in the cart it adds it.
        cart_details = {
            'quantity': 1,
            'size': Size.objects.filter(format_name=product.aspect_ratio).first().size_name,
            'technology': 'Photo Print',
            'unit_price': float(product.base_repro_fee)
        }
        cart[id] = cart_details 

    request.session['cart'] = cart

    return redirect(reverse('products'))





def update_cart(request, id):
    """ Updating thecart with the selected print technology and size 
    of the item selected in the form and redirects to the page  """

    # extract data from the request
    selected_size = request.POST.get('size')
    selected_tech = request.POST.get('technology')
    selected_product = get_object_or_404(Product, pk=id)
    qty = int(request.POST.get('quantity'))

    print(f"size: {selected_size}, tech: {selected_tech}, prod {selected_product} and qty: {qty} coming from form")

    # calculate the shorter and longer size dimensions
    ss = int(selected_size.split()[0])
    ls = int(selected_size.split()[2])

    # define the technologies coefficient from the tech selected
    if selected_tech == "Photo Print":
        tech_coeff = 1
    elif selected_tech == "Canvas Print":
        tech_coeff = 2.1
    elif selected_tech == "Metal Print":
        tech_coeff = 3.2
    elif selected_tech == "Acrylic Print":
        tech_coeff = 1.4
    elif selected_tech == "Framed Print":
        tech_coeff = 1.8
    else:
        tech_coeff = 1

    # get the base repro_fee from the Product model
    base_repro_fee = float(selected_product.base_repro_fee)

    # reproduction fee increases by size:
    repro_fee = (base_repro_fee) + round(( ls * ss ) / 300)

    # calculate the price of one item with the selectes size and technology
    diagonal = math.sqrt( ss * ss + ls * ls)
    unit_price = round( diagonal / 10 * 2 * tech_coeff + repro_fee ) - 0.01

    # PRICE CALCULATION DONE CART MANIPULATION BELOW

    cart = request.session.get('cart', {})
    cart_details = {
        'quantity': qty,
        'size': selected_size,
        'technology': selected_tech,
        'unit_price': unit_price,
    }
    print(f"size: {selected_size}, tech: {selected_tech}, prod {selected_product} and qty: {qty} coming from form")
    if qty > 0:
        cart[id] = cart_details 
    else:
        cart.pop(id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
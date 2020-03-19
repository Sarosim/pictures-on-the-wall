from django.shortcuts import render, redirect, reverse

# Create your views here.

def view_cart(request):
    """ Rendering the shopping cart contents page """
    return render(request, "cart.html")


def add_to_cart(request, id):
    """ Adds the product to the cart and redirects to the page.
    (no quantity is obtained, as 99.99% of the customers will buy only one copy of the artwork)"""

    cart = request.session.get('cart', {})
    
    if id in cart:
        # If the product is in the cart already, it increases the quantity 
        cart[id] = int(cart[id]) + 1      
    else:
        # If it's not in the cart it add it.
        cart[id] = cart.get(id, 1) 

    request.session['cart'] = cart
    return redirect(reverse('products'))


def adjust_cart(request, id):
    """ Adjusts the quantity of the item selected in the form and redirects to the page  """
    new_quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if new_quantity > 0:
        cart[id] = new_quantity
        print('cart[id] after change: ', cart[id])
    else:
        cart.pop(id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
from django.shortcuts import render, redirect, reverse

# Create your views here.

def view_cart(request):
    """ Rendering the shopping cart contents page """
    return render(request, "cart.html")


def add_to_cart(request, id):
    """ Adds the quantity of the item selected in the form and redirects to the page """
    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] = int(cart[id]) + quantity      
    else:
        cart[id] = cart.get(id, quantity) 

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
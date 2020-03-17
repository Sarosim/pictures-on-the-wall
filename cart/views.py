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
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    print(quantity)
    print(cart[id])


    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
    return redirect(reverse('view_cart'))
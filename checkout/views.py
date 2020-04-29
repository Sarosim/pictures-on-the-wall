from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem
from products.models import Product
from django.conf import settings
from django.utils import timezone
import stripe

# Create your views here.

stripe.api_key = settings.STRIPE_SECRET

@login_required()
def checkout(request):
    """ The checkout form - requires the user to be logged in """
    if request.method=="POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)
        
        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()
            
            cart = request.session.get('cart', {})

    #         number = selected_product.num_of_views + 1
    # Product.objects.filter(pk=id).update(num_of_views=number)


            total = 0
            for id, details in cart.items():
                product = get_object_or_404(Product, pk=id)
                qty = details['quantity']
                size = details['size']
                technology = details['technology']
                unit_price = details['unit_price']
                total += qty * unit_price

                order_line_item = OrderLineItem(
                    order = order, 
                    product = product, 
                    quantity = qty
                    )
                order_line_item.save()
                # Update product with number of items sold
                num = product.num_of_orders + qty
                Product.objects.filter(pk=id).update(num_of_orders=num)
                
            try:
                customer = stripe.Charge.create(
                    amount = int(total * 100),
                    currency = "GBP",
                    description = request.user.email,
                    card = payment_form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:
                messages.error(request, "Your card has been declined!")
                
            if customer.paid:
                messages.error(request, "You have successfully paid!")
                request.session['cart'] = {}
                return redirect(reverse('home'))
            else:
                messages.error(request, "Unable to take payment!")
        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to take a payment with that card!")
    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm()
        
    return render(request, "checkout.html", {'order_form': order_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE})
                
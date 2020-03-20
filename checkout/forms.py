from django import forms
from .models import Order
import datetime


class MakePaymentForm(forms.Form):
    """ The form for the customer to enter payment details """

    start_year = datetime.datetime.now().year
    end_year = start_year + 19

    MONTH_CHOICES = [(i, i) for i in range(1, 12)]
    YEAR_CHOICES = [(i, i) for i in range(start_year, end_year)]

    credit_card_number = forms.CharField(label='Credit card number', required=False)
    cvv = forms.CharField(label='Security code - CVV', required=False)
    expiry_month = forms.ChoiceField(label='Exp. Month', choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(label='Exp. Year', choices=YEAR_CHOICES, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)


class OrderForm(forms.ModelForm):
    """ The form for the customer to enter order details """

    class Meta:
        model = Order
        fields = (
            'first_name', 'last_name', 'phone_number', 'country', 'postcode',
            'town_or_city', 'address_line1', 'address_line2'
        )

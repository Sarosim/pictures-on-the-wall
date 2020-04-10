from django.shortcuts import render, redirect
from django.urls import reverse
from products.models import Product, Category, Hashtag, Rating, Artist
from django.contrib.auth.decorators import login_required
# from pictures_on_the_wall.utils import special_filter

# Create your views here.

@login_required
def dashboard(request):
    """ The view rendering the Arist dashboard """
    return render(request, 'dashboard.html')
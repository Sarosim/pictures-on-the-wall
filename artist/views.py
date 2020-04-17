from django.shortcuts import render, redirect
from django.urls import reverse
from products.models import Product, Category, Hashtag, Rating, Artist
from .forms import ArtistProfileForm
from products.forms import EditProductFormOne, EditProductFormThree
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from pictures_on_the_wall.utils import get_the_ratings_for

# Create your views here.


@login_required
def dashboard(request):
    """ The view rendering the Arist dashboard """
    # Getting the logged in user from the request
    # and finding the corresponding artist in the Artist model
    set_artist = Artist.objects.filter(assigned_user=request.user)
    if set_artist:
        # The logged in user has an artist associated 
        set_artist_id = set_artist.values('id')[0]['id']
        selected_products = Product.objects.filter(artist=set_artist_id)
        ratings_list = []
        sum_rate = 0
        for prod in selected_products:
            prod_ratings = get_the_ratings_for(prod)
            ratings_list.append(prod_ratings)
            sum_rate += prod_ratings['ratings_average']
        print(sum_rate, selected_products)
        avrg_rate = round(sum_rate / len(ratings_list), 2) if len(ratings_list) > 0 else 0
        page_data = {
            'artist': set_artist,
            'products': selected_products,
            'average_rating': avrg_rate,
        }
    else:
        # The logged in user doesn't have an artist profile")
        # Create an empty Profile form instance (with id)
        artist_form = ArtistProfileForm(
            initial={'assigned_user': request.user.id})
        # give them a message to create one
        messages.error(request, "Please create your Artist profile first!")
        return render(request, "artist_profile.html", {'artist_form': artist_form})

    return render(request, 'dashboard.html', {'page_data': page_data})


@login_required
def artist_profile(request):
    """ The view rendering the page for Artist profile creation, modification
    or deletion """
    if request.method == 'POST':
        # User submitted an Artist profile form
        artist_form = ArtistProfileForm(request.POST)
        if artist_form.is_valid():
            # Save the form
            artist_form.save()
            
            return redirect('dashboard')
        else:
            print("Form isn't valid, to be handled later")
    
    else:
        # Check whether user has an artist profile
        if Artist.objects.filter(assigned_user=request.user):
            # get the artist id
            set_artist = Artist.objects.filter(
                assigned_user=request.user).values('id')[0]['id']
            # pick the corresponding record from Artist model
            my_record = Artist.objects.get(id=set_artist)
            # Set the form instace
            artist_form = ArtistProfileForm(instance=my_record)
        else:
            # Set an empty Profile form instance (with hidden user id)
            artist_form = ArtistProfileForm(
                initial={'assigned_user': request.user.id})

    # Populate the form on the template
    return render(request, 'artist_profile.html', {'artist_form': artist_form})

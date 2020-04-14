from django.shortcuts import render, redirect
from django.urls import reverse
from products.models import Product, Category, Hashtag, Rating, Artist
from .forms import ArtistProfileForm
from products.forms import EditProductFormOne, EditProductFormThree
from django.contrib.auth.decorators import login_required
# from pictures_on_the_wall.utils import special_filter

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
        print(f"Artist {set_artist} has {set_artist_id} id")
        selected_products = Product.objects.filter(artist=set_artist_id)
        print(selected_products)
        page_data = {
            'artist': set_artist,
            'products': selected_products,
        }
        return render(request, 'dashboard.html', {'page_data': page_data})
    else:
        # The logged in user doesn't have an artist profile")
        # Create an empty Profile form instance (with id)
        artist_form = ArtistProfileForm(
            initial={'assigned_user': request.user.id})
        return render(request, "artist_profile.html", {'artist_form': artist_form})

    return render(request, 'dashboard.html')


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
            # Prepare the form for uploading a new artwork and render the page
            set_artist = Artist.objects.filter(
                assigned_user=request.user).values('id')[0]['id']
            edit_form_one = EditProductFormOne(initial={'artist': set_artist})
            edit_form_three = EditProductFormThree()
            return render(request, 'edit.html',
                {
                    'edit_form_one': edit_form_one,
                    'edit_form_three': edit_form_three,
                }
                )
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

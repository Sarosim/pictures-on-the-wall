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
        # An empty Profile form instance (with id)
        artist_form = ArtistProfileForm(
            initial={'assigned_user': request.user.id})

    return render(request, 'artist_profile.html', {'artist_form': artist_form})

from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Product, Category, Hashtag, Rating, Artist, Size
from .forms import FileUploadForm  # probably superseded, to be deleted
from .forms import EditProductFormOne, EditProductFormThree, ArtistProfileForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def all_products(request):
    """ The view rendering a page with all products listed """
    all_the_products = Product.objects.all()
    return render(request, "products.html", {"products": all_the_products})


def product_details(request, id):
    """ The view rendering the page for one selected
    product and all of its details """
    selected_product = Product.objects.get(pk=id)
    # filtering the hashtags associated with the selected product:
    hashtags = Hashtag.objects.filter(product=selected_product)
    # filtering all the relevant ratings from the Rating model:
    ratings = Rating.objects.filter(product=selected_product)
    ratings_total = 0
    ratings_count = 0
    if ratings:
        for rating in ratings:
            ratings_total += rating.rating
            ratings_count += 1
        ratings_average = ratings_total / ratings_count
    else:
        ratings_average = 0
    ratings_percent = round(ratings_average * 20)
    ratings_data = {
        "ratings_average": ratings_average,
        "ratings_percent": ratings_percent,
        "ratings_count": ratings_count
    }
    # Bundling the data for the template to a dictionary:
    pass_to_template = {
        "selected_prod": selected_product,
        "hashtags": hashtags,
        "ratings_data": ratings_data
    }
    return render(
        request,
        "product_details.html",
        {"pass_to_template": pass_to_template}
    )


def filtered_products(request, filter_group, filter_name):
    """ The view rendering a page for all products (Artwork)
    filtered by a user selected criteria """

    # setting the values for the variables 'manually'
    # before actual links properly set on page
    filter_group = 'room'
    filter_name = 'bathroom'

    # constructing kwargs for the filter
    if filter_group == 'hashtag':
        # the hashtag model doesn't have a hashtag_name field
        filter_subgroup = 'hashtag'
    else:
        # we use the 'model'+'_name' fields from the other models
        filter_subgroup = filter_group + '_name'
    
    # the actual keyword argument for the filtering:
    filter_kwargs = filter_group + '__' + filter_subgroup + '__' + 'iexact'

    # the actual filtering
    filtered_products = Product.objects.filter(**{filter_kwargs: filter_name})

    return render(request, "products.html", {"products": filtered_products})


@login_required
def file_upload(request):
    """ The view rendering the page that explains how to become a contributor
    and upload an image, as well we the form for file upload"""
    return render(request, 'upload.html')


@login_required
def edit_artwork(request):
    """ The view rendering a page for providing details for, or editing the 
    details of uploaded Artwork """

    if request.method == 'POST':
        # If the form is being submitted:
        # create a form instance and populate it with data from the request:

        edit_form_one = EditProductFormOne(request.POST, request.FILES)
        edit_form_three = EditProductFormThree(request.POST)

        # Getting the logged in user from the request
        # and finding the corresponding artist in the Artist model
        set_artist = Artist.objects.filter(assigned_user=request.user)
        # getting their id from the QuesrySet
        set_artist = set_artist.values('id')[0]['id']

        if edit_form_one.is_valid() and edit_form_three.is_valid():
            # save the form of the Product model
            edit_form_one.save()

            # The #hashtags need to be handled - TO BE IMPLEMENTED...
            # edit_form_three.save()
            # redirect to the products page with all the products listed
            # - this will need adjusting FOR the FINAL VERSION...
            all_the_products = Product.objects.all()
            return render(request, 'products.html', {"products": all_the_products})
        else:
            print(f"file upload form isn't valid  - no file saved")

    else:
        # if the request is GET
        try:
            # First check whether the user has an Artist profile:
            set_artist = Artist.objects.filter(
                assigned_user=request.user).values('id')[0]['id']
        except:
            # No Artist exists for the current user -> redirect them to create
            artist_form = ArtistProfileForm(
                initial={'assigned_user': request.user.id})
                # create a blank form with the artist prepopulated with a HiddenInput
            return render(request, 'artist_profile.html', {'artist_form': artist_form})
        
        edit_form_one = EditProductFormOne(initial={'artist': set_artist})
        edit_form_three = EditProductFormThree()

    return render(
        request,
        'edit.html',
        {
            'edit_form_one': edit_form_one,
            'edit_form_three': edit_form_three,
        }
    )

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

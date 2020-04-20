from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Product, Category, Hashtag, Rating, Artist, Size, Format, Technology
from .forms import FileUploadForm  # probably superseded, to be deleted
from .forms import EditProductFormOne, EditProductFormThree
from artist.forms import ArtistProfileForm
from django.contrib.auth.decorators import login_required
from pictures_on_the_wall.utils import special_filter, get_the_ratings_for
from django.contrib import messages
from django.contrib.auth.models import User
from .utils import image_manipulation, create_size_entries

# Create your views here.


def all_products(request):
    """ The view rendering a page with all products listed """
    all_the_products = Product.objects.all()
    return render(request, "products.html", {"products": all_the_products})


def product_details(request, id):
    """ The view rendering the page for one selected
    product and all of its details """
    selected_product = get_object_or_404(Product, id=id)
    
    # get existing number of views, increment and update model
    number = selected_product.num_of_views + 1
    Product.objects.filter(pk=id).update(num_of_views=number)

    # filtering the hashtags associated with the selected product:
    hashtags = Hashtag.objects.filter(product=selected_product)
    
    # filtering all the relevant ratings from the Rating model:
    ratings_data = get_the_ratings_for(selected_product)

    # filtering all the sizes from the Size model:
    sizes = Size.objects.filter(format_name=selected_product.aspect_ratio)
    print(f"SIZES: {sizes}")

    technologies = Technology.objects.all()

    # Bundling the data for the template to a dictionary:
    pass_to_template = {
        "selected_prod": selected_product,
        "hashtags": hashtags,
        "ratings_data": ratings_data,
        'sizes': sizes,
        'technologies': technologies,
    }
    return render(
        request,
        "product_details.html",
        {"pass_to_template": pass_to_template}
    )


def filtered_products(request, filter_group, filter_name):
    """ The view rendering a page for all products (Artwork)
    filtered by a user selected criteria """

    # Call my helper function in utils.py to run the filter
    filtered_products = special_filter(filter_group, filter_name)

    return render(request, "products.html", {"products": filtered_products})


@login_required
def file_upload(request):
    """ The view rendering the page that explains how to become a contributor
    and upload an image, as well as the form for file upload"""


    if request.method == 'POST':
        edit_form_one = EditProductFormOne(request.POST, request.FILES)
        edit_form_three = EditProductFormThree(request.POST)

        set_artist = Artist.objects.filter(assigned_user=request.user)
        set_artist = set_artist.values('id')[0]['id']

        if edit_form_one.is_valid() and edit_form_three.is_valid():
            uploaded_file = request.FILES['image']
            image_data = image_manipulation(uploaded_file)
            new_product = edit_form_one.save(commit=False)
            new_product.aspect_ratio = Format.objects.get(id=image_data['format_id'])
            new_product.max_print_size = image_data['longer_side']
            new_product.save()
            edit_form_one.save_m2m()
            
            
            # The #hashtags need to be handled - TO BE IMPLEMENTED...
            # edit_form_three.save()
            # redirect to the products page with all the products listed


            return redirect('dashboard')
        else:
            print(f"file upload form isn't valid  - no file saved")

    else:
        try:
            # First check whether the user has an Artist profile:
            set_artist = Artist.objects.filter(
                assigned_user=request.user).values('id')[0]['id']
        except:
            # No Artist exists for the current user -> redirect them to create
            # with a message about the reason
            messages.success(request, "In order to be able to upload an artwork you need an Artist profile. Please create yours!")
            artist_form = ArtistProfileForm(
                initial={'assigned_user': request.user.id})
                # create a blank form with the artist prepopulated with a HiddenInput
            return render(request, 'artist_profile.html', {'artist_form': artist_form})
        
        edit_form_one = EditProductFormOne(initial={'artist': set_artist})
        edit_form_three = EditProductFormThree()

    return render(
        request,
        'upload.html',
        {
            'edit_form_one': edit_form_one,
            'edit_form_three': edit_form_three,
        }
    )


def modify_artwork(request, id):
    """ The view rendering a page for modifying an already uploaded artwork\n
    pre-populates a form with the product selected by the user and saves the POST"""
    selected_product = get_object_or_404(Product, id=id)
    print(selected_product)

    if request.method == 'POST':
        # If the form is being submitted:
        # create a form instance and populate it with data from the request:

        edit_form_one = EditProductFormOne(request.POST, request.FILES, instance=selected_product)
        edit_form_three = EditProductFormThree(request.POST, instance=selected_product)
        if edit_form_one.is_valid() and edit_form_three.is_valid():
            # get the file from the request
            uploaded_file = request.FILES['image']
            # send it to my Pillow utility function to process
            image_data = image_manipulation(uploaded_file)
            # get an object that hasn’t yet been saved to the database
            new_product = edit_form_one.save(commit=False)
            # save the extra fields:
            new_product.aspect_ratio = Format.objects.get(id=image_data['format_id'])
            new_product.max_print_size = image_data['longer_side']
            # ... more to be done here ... 
            # save the modifications
            new_product.save()
            # Now, save the many-to-many data for the form:
            edit_form_one.save_m2m()
            
            # The #hashtags need to be handled here ...  - TO BE IMPLEMENTED...
            return redirect('dashboard')
        else:
            print(f"file upload form isn't valid  - no file saved")

    else:
        # if the request is GET
        # Check whether the Product with the id belongs to the user
        set_artist = Artist.objects.filter(
                assigned_user=request.user)
        product_artist = selected_product.artist
        if set_artist.values('id')[0]['id'] == product_artist.id:
            edit_form_one = EditProductFormOne(instance=selected_product)
            edit_form_three = EditProductFormThree(instance=selected_product)
        else:
            messages.error(request, "It's interesting how you ended up here... ")
            messages.error(request, "... either something went wrong on our side or you are trying to be cheeky.")
            return redirect(reverse('home'))
        
    return render(request, 'modify.html',
        {
            'edit_form_one': edit_form_one,
            'edit_form_three': edit_form_three,
            'product': selected_product
        })


@login_required
def delete_artwork(request, id):
    """ A function handling a deleting request for an artwork\n
    displaying a confirmation page if the user is aloowed to delete"""
    artwork = get_object_or_404(Product, pk=id)
    # first we check if the user is the "owner" of the image
    artist = artwork.artist
    user = request.user
    if artist.assigned_user == user:
        #if yes, we display the confirmation page
        return render(request, 'delete_confirm.html', {'product': artwork}) 
    else:
        # otherwise we let them know:
        messages.error(request, 'Sorry It seems you are trying to delete a product that is not yours...')
    
    user = User.objects.get(email=request.user.email)
    return render(request, 'profile.html', {"profile": user})


@login_required
def delete_confirm(request, id):
    """ Actually deleting after confirmation\n
    using a form with post method to confirm deletion """
    artwork = get_object_or_404(Product, pk=id)
    if request.method == 'POST':
        artist = artwork.artist
        artist_queryset = Artist.objects.filter(id=artist.id)
        try:
            artwork.delete()
        except:
            messages.error(request, "Error! We could't delete the specified artwork")
        print(f"{artwork} DELETED") # UNCOMMENT THE DELETE FOR THE PRODUCTION VERSION OR WHEN FINISHED TESTING ITS FUNCTIONALITY!!!!!
        selected_products = Product.objects.filter(artist=artist.id)
        # collect information for dashboard and re-render the page
        page_data = {
            'artist': artist_queryset,
            'products': selected_products,
        }
        return render(request, 'dashboard.html', {'page_data': page_data})
    else:
        # send a message to the tempering 'user' that it won't work...
        messages.error(request, 'Nice try ... but you are not allowed to delete that product')
    
    user = User.objects.get(email=request.user.email)
    return render(request, 'profile.html', {"profile": user})
from django.shortcuts import render
from products.models import Artist, Category, Room, Hashtag
from django.db import models
from django.apps import apps

def index(request):
    """A view that displays the landing page"""
    return render(request, "index.html")

def index_no_intro(request, filter_group="category"):
    """The view that displays the landing page without the intro, so users
    already on the page don't get disrupted bu the intro every time
    they go back to the home page"""
    # Different filtering can be selected, therefore links and page content 
    # need presetting
    possible_filters = (
        "category",
        "artist",
        "room",
        "hashtag"
    )
    others = []
    # creating a list for the unselected potential other filters
    for filt in possible_filters:
        if filt == filter_group:
            continue
        else:
            others.append(filt)
    
    # Pick the Model for the selected filter
    SelectedModel = apps.get_model('products', filter_group)

    # collecting the instances from the selected model
    filter_group_queryset = SelectedModel.objects.all()

    if SelectedModel == Hashtag:
        print("Hashtag selected, need action to limit list to unique items")
        # NEED TO DO SOMETHING WITH HASHTAGS to pick one from each 

    page_structure = {
        'filter_by': filter_group,
        'others': others,
        'filter_group_queryset': filter_group_queryset
    }

    return render(request, 'index_no_intro.html', {'page_structure': page_structure})

from django.shortcuts import render
from products.models import Artist, Category, Room, Hashtag
from django.db import models
from django.apps import apps
from pictures_on_the_wall.utils import special_filter

def index(request):
    """A view that displays the landing page"""
    return render(request, "index.html")

def index_no_intro(request, filter_group="category"):
    """The view that displays the landing page without the intro, so users
    already on the page don't get disrupted by the intro every time
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
    print(f"SelectedModel {SelectedModel}")
    # collecting the instances from the selected model
    filter_group_queryset = SelectedModel.objects.all()
    print(f"filter_group_queryset: a selected modelbol minden Product {filter_group_queryset}")
    # create a list of sample Products that represents each instance in the model
    sample_list = []
    for item in filter_group_queryset:
        sample_prod = special_filter(filter_group, str(item)).order_by('id').first()
        sample_list.append(sample_prod)

    # organise the QuerySets and the sample Products into a list of lists,
    # so it is easy to handle on the frontend in a for loop
    items = []
    for i, item in enumerate(filter_group_queryset):
        # each inner list consists of the QuerySet item and the corresponding sample
        items.append([item, sample_list[i]])

    if SelectedModel == Hashtag:
    print("Hashtag selected, THIS IS NOT GOOODDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD")
    # HASHTAGS to be excluded from filtering 

    page_structure = {
        'filter_by': filter_group,
        'others': others,
        'items': items
    }

    print(page_structure)

    return render(request, 'index_no_intro.html', {'data': page_structure})

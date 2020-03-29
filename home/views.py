from django.shortcuts import render
from products.models import Artist, Category, Room, Hashtag

def index(request):
    """A view that displays the landing page"""
    return render(request, "index.html")

def index_no_intro(request, filter_group="category"):
    """The view that displays the landing page without the intro, so users already on the page /
    don't get disrupted bu the intro every time they go back to the home page"""
    others = []
    possible_filters = (
        "category",
        "artist",
        "room",
        "hashtag"
    )
    for filt in possible_filters:
        if filt == filter_group:
            filter_by = filt
        else:
            others.append(filt)

    # all_categories = Category.objects.all()
    # all_artists = Artist.objects.all()
    # all_rooms = Room.objects.all()
    # all_hashtags = Hashtag.objects.all()
    # filter_by = filter_group

    page_structure = {
        'filter_by': filter_by,
        'others': others
    }

    return render(request, 'index_no_intro.html', {'page_structure': page_structure})

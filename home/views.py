from django.shortcuts import render

def index(request):
    """A view that displays the landing page"""
    return render(request, "index.html")

def index_no_intro(request):
    """The view that displays the landing page without the intro so users already on the page /
    don't get disrupted bu the intro every time they go back to the home page"""
    return render(request, 'index_no_intro.html')

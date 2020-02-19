from django.shortcuts import render

def index(request):
    """A view that displays the landing page"""
    return render(request, "index.html")

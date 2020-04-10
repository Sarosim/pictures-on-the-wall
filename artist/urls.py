from django.conf.urls import url, include
from .views import dashboard, artist_profile

urlpatterns = [
    url(r'^$', dashboard, name = 'dashboard'),
    url(r'^artist_profile/', artist_profile, name = "artist_profile"),
]
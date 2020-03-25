from django.conf.urls import url
from .views import search_by_title

urlpatterns = [
    url(r'^$', search_by_title, name = 'search'),
]
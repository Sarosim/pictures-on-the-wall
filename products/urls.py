from django.conf.urls import url, include
from products.views import all_products, product_details, filtered_products, file_upload, modify_artwork, delete_artwork, delete_confirm, rate_artwork, sort_and_filter

urlpatterns = [
    url(r'^$', all_products, name = 'products'),
    url(r'^filtered/(?P<filter_group>\w*)/(?P<filter_name>\W*\w*)/(?P<sort_by>\w*)', filtered_products, name = "filtered_products"),
    url(r'^filtered/', filtered_products, name = "filtered_products"),
    url(r'^product_details/(?P<id>\d+)', product_details, name = "product_details"),
    url(r'^upload/', file_upload, name = "file_upload"),
    url(r'^modify/(?P<id>\d+)', modify_artwork, name = "modify_artwork"),
    url(r'^delete/(?P<id>\d+)', delete_artwork, name = "delete_artwork"),
    url(r'^delete_confirm/(?P<id>\d+)', delete_confirm, name = "delete_confirm"),
    url(r'^rate/(?P<id>\d+)', rate_artwork, name = "rate_artwork"),
    url(r'^rate/', rate_artwork, name = "rate_artwork"),
    url(r'^sort/', sort_and_filter, name = "sort"),
]
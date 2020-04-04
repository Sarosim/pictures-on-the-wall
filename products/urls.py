from django.conf.urls import url, include
from products.views import all_products, product_details, filtered_products, file_upload

urlpatterns = [
    url(r'^$', all_products, name = 'products'),
    url(r'^filtered/(?P<filter_group>\w+)/(?P<filter_name>\w+)', filtered_products, name = "filtered_products"),
    url(r'^product_details/(?P<id>\d+)', product_details, name = "product_details"),
    url(r'^upload/', file_upload, name = "file_upload"),
]
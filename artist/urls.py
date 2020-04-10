from django.conf.urls import url, include
from .views import dashboard

urlpatterns = [
    url(r'^$', dashboard, name = 'dashboard'),
]
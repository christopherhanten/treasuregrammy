# main_app/urls.py
from django.conf.urls import url
from .views import index
from .views import show
from .views import post_treasure

urlpatterns = [
    url(r'^$', index),
    url(r'^([0-9]+)/$', show, name = 'show'),
    url(r'^post_url/$', post_treasure, name="post_treasure")
]

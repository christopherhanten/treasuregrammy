# main_app/urls.py
from django.conf.urls import url
from .views import index
from .views import show
from .views import post_treasure
from .views import profile
from .views import login_view
from .views import logout_view


urlpatterns = [
    url(r'^user/(\w+)/$', profile, name='profile'),
    url(r'^$', index),
    url(r'^([0-9]+)/$', show, name = 'show'),
    url(r'^post_url/$', post_treasure, name="post_treasure"),
    url(r'^login/$', login_view, name="login"),
    url(r'^logout/$', logout_view, name="logout"),
]

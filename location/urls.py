from django.conf.urls import patterns, url
from .views import index, place_index, categorise_post
# from location import views

urlpatterns = [
    url(r'^$', index, name = "index"),
    url(r'^location/(?P<place_id>[0-9]+)/$', place_index, name="place_index"),
    # url(r'^location/(?P<place_id>[0-9]+)categorise_post/categorise/new/$', new_post, name="new_post"),
    url(r'^location/(?P<place_id>[0-9]+)/categorise(?:/(?P<post_id>[0-9]+))?/$', 
    	categorise_post, name="categorise_post"),
]

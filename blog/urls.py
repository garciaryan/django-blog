from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^toggle-like$', views.toggle_like, name='toggle_like'),
]

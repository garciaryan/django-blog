from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^(?P<post_id>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^toggle-like/(?P<post_id>\d+)/$', views.toggle_like, name='toggle_like'),
]

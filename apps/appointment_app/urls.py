from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.user, name = 'user'),
    url(r'^/new$', views.new, name = 'new'),
    url(r'^/(?P<id>\d+)/show$', views.show),
    url(r'^/(?P<id>\d+)/update$', views.update, name ='update'),
    url(r'^/(?P<id>\d+)/edit/$', views.edit),
    url(r'^/(?P<id>\d+)/destroy/$', views.destroy),
]

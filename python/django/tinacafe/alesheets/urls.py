from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
                       url(r'^$', views.index),
                       url(r'^account/(?P<short_name>\S+)/$', views.show_account),
                       )

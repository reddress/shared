from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^view_diary/$', views.view_diary,
                           name='view_diary'),
                       url(r'^view_entry/$', views.view_entry,
                           name='view_entry'),
                       url(r'^search/$',
                           views.search,
                           name='search'),
                       )

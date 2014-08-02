from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^post/(?P<post_id>\d+)/$', views.view_post,
                           name='view_post'),
                       
                       )

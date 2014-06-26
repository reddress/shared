from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from .views import do_logout

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'heitor.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

                       url(r'^$', 'heitor.views.index', name='root'),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^howifeel/', include('howifeel.urls')),
                       url(r'^accounts/login/$', 'django.contrib.auth.views.login', name='login'),
                       url(r'^accounts/logout/$', do_logout, name='logout'),
)

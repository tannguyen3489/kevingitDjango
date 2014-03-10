from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'kevincms.views.home', name='home'),
    url(r'view/$', 'kevincms.views.view', name='view'),
    url(r'adminpage/$', 'kevincms.views.admin', name='admin'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

)

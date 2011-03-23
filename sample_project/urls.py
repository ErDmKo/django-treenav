from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('sample_project.views',
    # Example:
    # (r'^sample_project/', include('sample_project.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^treenav/', include('treenav.urls.admin')),
    (r'^treenav-missing/', include('treenav.urls.undefined_url')),
    url(r'^$', 'home', name='home'),
    url(r'^about/$', 'home', name='about'),
    url(r'^test/$', 'home', name='test'),
)

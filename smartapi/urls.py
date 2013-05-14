# -*- coding:utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'smartapi.views.home', name='home'),
    # url(r'^smartapi/', include('smartapi.foo.urls')),
    #将不同的url解析为不同的服务
#    url(r'^auth/', 'smartapi.views.auth'),
#    url(r'^compute/', 'smartapi.views.auth'),
#    url(r'^image/', 'smartapi.views.image'),
#    url(r'^volume/', 'smartapi.views.volume'),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'smartapi.views.home'),
    url(r'^user/logon', 'smartapi.views.logon'),
    url(r'^user/logout', 'smartapi.views.logout'),
#    url(r'^api/$', 'smartapi.views.api'),
#    url(r'^api/auth/$', 'smartapi.views.api_auth'),
    #url(r'^api/images/(?P<id>.*)$', 'smartapi.views.image', name='api'),
#    url(r'^api/images/$', 'smartapi.views.images'),
#    url(r'^api/flavors/$', 'smartapi.views.flavors'),
#    url(r'^api/servers/$', 'smartapi.views.flavors'),
    #url(r'^monitor$', 'views.monitor', name='monitor'),
    url(r'^api/', 'smartapi.views.proxy'),
    url(r'^apidoc/$', 'smartapi.views.apidoc'),
    url(r'^apidoc/(?P<resource_id>\d+)/$', 'smartapi.views.apidoc'),
    url(r'^kvm/', 'smartapi.views.kvm'),
)
urlpatterns += staticfiles_urlpatterns()
from django.conf.urls import patterns, include, url

from django.contrib import admin

import stockdata

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'stockdata.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^index/(.+)/$', 'controler.index.search'),
    # url(r'^stati/(?P<path>.*)$','django.views.static.serve',{'document_root':stockdata.settings.STATICFILES_DIRS, 'show_indexes': True}),
)

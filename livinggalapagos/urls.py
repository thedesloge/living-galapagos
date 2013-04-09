from django.conf.urls import patterns, include, url
from django.conf import settings
from haystack.views import SearchView, search_view_factory
from haystack.query import SearchQuerySet
from haystack.forms import SearchForm,ModelSearchForm

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'testlivinggalapagos.views.home', name='home'),
    # url(r'^testlivinggalapagos/', include('testlivinggalapagos.foo.urls')),
    url(r'^grappelli/', include('grappelli.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('story_database.urls')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
    url(r'^api/', include('story_api.urls')),
)

urlpatterns += patterns('haystack.views',
    url(r'^search/$', search_view_factory(
        view_class=SearchView,
        template='story_database/search.html',
        form_class=SearchForm,                                           
        ),name='haystack_search'  )
)

from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('story_database.views',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^myproject/', include('myproject.foo.urls')),
    
     url(r'^$', 'home', name='home page english'),
     url(r'^(?P<language_code>en|es)/$', 'home', name="english or spanish home page"),
     url(r'^(?P<language_code>en|es)/article/(?P<article_slug>.*)/$', 'article_story_page', name="article story"),
     url(r'^(?P<language_code>en|es)/learn/(?P<story_slug>.*)/$', 'learn', name="learn"),
     url(r'^about/$', 'about'),
     url(r'^search/$', 'search'),
     url(r'^search/map/$', 'search_map'),
     url(r'^(?P<language_code>en|es)/search/$', 'search'),
     url(r'^(?P<language_code>en|es)/search/map/$', 'search_map'),
     url(r'^(?P<language_code>en|es)/about/', 'about'),
     url(r'^(?P<language_code>en|es)/(?P<story_slug>.*)/$', 'featured_story_page', name="featured story"),
     #url(r'^testing/$', 'testing'),
     
)

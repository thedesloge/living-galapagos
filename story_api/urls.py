from django.conf.urls import patterns, url, include
from rest_framework.urlpatterns import format_suffix_patterns
from story_api.views import *

urlpatterns = patterns('story_api.views',
    url(r'^$', 'api_root'),
    url(r'^stories/$', StoryList.as_view(), name='user-list'),
    url(r'^stories/(?P<pk>\d+)/$', StoryDetail.as_view(), name='user-detail'),
    url(r'^story-trans/$', StoryTranslationList.as_view(), name='story-trans-list'),
    url(r'^story-trans/(?P<pk>\d+)/$', StoryTranslationDetail.as_view(), name='story-trans-detail'),
    url(r'^videos/(?P<pk>\d+)/$', VideoDetail.as_view(), name='video-detail'),
    url(r'^categories/(?P<pk>\d+)/$', CategoryDetail.as_view(), name='category-detail'),
    url(r'^nav/$', NavView.as_view(), name='navigation'),
)

# Format suffixes
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])

# Default login/logout views
urlpatterns += patterns('',
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
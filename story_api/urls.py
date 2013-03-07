from django.conf.urls import patterns, url, include
from rest_framework.urlpatterns import format_suffix_patterns
from story_api.views import StoryList, StoryDetail

urlpatterns = patterns('story_api.views',
    url(r'^$', 'api_root'),
    url(r'^stories/$', StoryList.as_view(), name='user-list'),
    url(r'^stories/(?P<pk>\d+)/$', StoryDetail.as_view(), name='user-detail'),
)

# Format suffixes
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])

# Default login/logout views
urlpatterns += patterns('',
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
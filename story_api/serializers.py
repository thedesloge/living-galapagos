from story_database.models import *
from rest_framework import serializers

class StorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StoryPage
        fields = ('name','video')
        
class VideoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Video
        fields = ('name')

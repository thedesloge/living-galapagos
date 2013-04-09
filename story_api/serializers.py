from story_database.models import *
from rest_framework import serializers

class StoryTranslationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = StoryPageTranslation
        fields = ('description', 'headline')


class StorySerializer(serializers.ModelSerializer):
    translations = StoryTranslationSerializer(many=True)
    
    class Meta:
        model = StoryPage
        fields = ('name','video','category','thumbnail', 'interactives', 'translations')
        depth = 1
        
class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)
        
class VideoSerializer(serializers.HyperlinkedModelSerializer):
    title = serializers.CharField(source='slug', read_only=True)
    
    class Meta:
        model = Video
        
class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category

class MenuItemSerializer(serializers.ModelSerializer):
    page = StorySerializer()
    
    class Meta:
        model = MenuItem
        fields = ('name','name_es', 'url','position', 'page')
        depth = 1

class MenuSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    menuitem_set = MenuItemSerializer()
    class Meta:
        model = Menu
        depth = 1
        
    

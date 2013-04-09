from haystack import indexes
from haystack import site
from story_database.models import StoryPageTranslation

class StoryPageTranslationIndex(indexes.SearchIndex):
    text = indexes.CharField(document=True, use_template=True)
    headline = indexes.CharField(model_attr='headline')
    subheadline = indexes.CharField(model_attr='subheadline')
    single_line_description = indexes.CharField(model_attr='single_line_description')
    description = indexes.CharField(model_attr='description')
    story_thumbnail = indexes.CharField(model_attr='master')
    story_slug = indexes.CharField(model_attr='master')
    language = indexes.CharField(model_attr='language_code')
    
    
    def get_model(self):
        StoryPageTranslation
        
    def prepare_story_thumbnail(self, obj):
        return "%s" % obj.master.thumbnail.url
    
    def prepare_story_slug(self, obj):
        return "%s" % obj.master.slug
        
site.register(StoryPageTranslation, StoryPageTranslationIndex)
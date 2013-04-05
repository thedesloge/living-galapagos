from haystack import indexes
from haystack import site
from story_database.models import StoryPageTranslation

class StoryPageTranslationIndex(indexes.SearchIndex):
    text = indexes.CharField(document=True, use_template=True)
    headline = indexes.CharField(model_attr='headline')
    subheadline = indexes.CharField(model_attr='subheadline')
    description = indexes.CharField(model_attr='description')
    quote = indexes.CharField(model_attr='quote')
    quote_attribution = indexes.CharField(model_attr='quote_attribution')
    single_line_description = indexes.CharField(model_attr='single_line_description')
    
    def get_model(self):
        StoryPageTranslation
        
site.register(StoryPageTranslation, StoryPageTranslationIndex)
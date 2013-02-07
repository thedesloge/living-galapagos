"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from story_database.models import *
from zipfile import ZipFile
from django.core.files import File

class FeaturedPageTest(TestCase):
  fixtures = ['storyDump.json']
      
  def test_story(self):
      story = Story.objects.get(slug="story-one")
      self.assertEqual("story-one", story.slug, "message")
      
  def test_stories_in_category(self):
      language = "en"
      retVal = []
      story = Story.objects.get(pk=1)
      
      storiesInCategory = Story.objects.filter(category=story.category)
      print storiesInCategory
      try:
        for story in storiesInCategory:
          storyTrans = Story_Translation.objects.get(parent=story, language_code=language)
          print storyTrans
          retVal.append(storyTrans)
      except Story_Translation.DoesNotExist:
        pass
    
      return retVal
  
  def test_category(self):
      tempCategory = Category.objects.filter(slug="category-sea")
      for category in tempCategory:
          print category.slug
          


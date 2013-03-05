"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from django.utils import unittest
from django.test import TestCase
from story_database.models import *
from zipfile import ZipFile
from django.core.files import File


class FeaturedPageTestCase(TestCase):
  fixtures = ['testdump.json',]
  
  
  def test_get_featured_pages(self):
    main_page_features = FeaturedStory.objects.get(name="Main Page")
    self.assertEqual('Main Page', main_page_features.name)
    self.assertEqual(1, main_page_features.featuredstoryitem_set.count(), "There should be only one")
    
    featuredStories = FeaturedStory.objects.get(name="Main Page")
    story_page = featuredStories.featuredstoryitem_set.all()[0].page
    
    print story_page.translations.get(language_code='sp').headline

  def test_video_thumbnail(self):
      featured_story_collection = FeaturedStory.objects.get(name="Main Page")
      story = featured_story_collection.featuredstoryitem_set.all()[0].page
      print story.video
import os
import zipfile
import datetime
from django.db import models
from hvad.models import TranslatableModel, TranslatedFields
from language_test.zipstorage import ZipStorage
from django.core.files.storage import FileSystemStorage
from django.template.defaultfilters import slugify

def common_translated_fields():
  return TranslatedFields(
    headline = models.CharField(max_length=255, verbose_name=u'* Title/Headline'),
    subheadline = models.CharField(max_length=255, blank=True, null=True, verbose_name=u'* Subheadline'),
    description = models.TextField(verbose_name=u'* Description'),
    single_line_description = models.CharField(max_length=300, blank=True, null=True, verbose_name=u'* Single Line Description (Optional)'),
    quote = models.TextField(blank=True, null=True, verbose_name=u'* Quote (Optional)'),
    quote_attribution = models.TextField(blank=True, null=True, verbose_name=u'* Attribution (Optional)'),
  )

class Category(models.Model):
  class Meta:
    verbose_name = 'Category'
    verbose_name_plural = 'Categories'

  name = models.CharField(max_length=200)
  slug = models.SlugField()

  def __unicode__(self):
    return "Category: " + self.name
  
  @staticmethod
  def autocomplete_search_fields():
    return ("id__iexact", "name__icontains",)
  
class Tag(TranslatableModel):
  name = models.CharField(max_length=100)
  slug = models.SlugField()
  
  translations = TranslatedFields(
    translated_name = models.CharField(max_length=100, verbose_name=u"* Translated Name (shown on website)")
  )
  
  def __unicode__(self):
    return "Tag: " + self.name
  
  @staticmethod
  def autocomplete_search_fields():
    return ("id__iexact", "name__icontains",)

# Create your models here.
class Video(TranslatableModel):
  creation_date = models.DateField(auto_now_add=True)
  last_modified = models.DateField(auto_now=True)
  name = models.CharField(max_length=100, unique=True)
  author = models.CharField(max_length=255)
  category = models.ForeignKey('Category')
  thumbnail = models.FileField(upload_to='uploads/video/thumbnails/%Y/%m/%d', blank=True, null=True, verbose_name=u'Thumbnail (Optional)')
  
  translations = TranslatedFields(
    headline = models.CharField(max_length=255, verbose_name=u'* Title/Headline'),
    subheadline = models.CharField(max_length=255, blank=True, null=True, verbose_name=u'* Subheadline'),
    description = models.TextField(verbose_name=u'* Description'),
    single_line_description = models.CharField(max_length=300, blank=True, null=True, verbose_name=u'* Single Line Description (Optional)'),
    vimeo_id = models.IntegerField(verbose_name=u'* Vimeo ID'),
    poster_frame = models.FileField(upload_to='uploads/posterframes/%Y/%m/%d')
  )
  
  def __unicode__(self):
    return self.name
  
  @staticmethod
  def autocomplete_search_fields():
    return ("id__iexact", "name__icontains",)

class Poster_Frame(models.Model):
  class Meta:
    verbose_name = "Poster Frame"
    verbose_name_plural = "Poster Frames"

  name = models.CharField(max_length=200, unique=True)
  slug = models.SlugField()
  poster_frame = models.FileField(upload_to='uploads/posterframes/%Y/%m/%d')
  
  def __unicode__(self):
    return self.name
  
  @staticmethod
  def autocomplete_search_fields():
    return ("id__iexact", "name__icontains",)
 
class Interactive(TranslatableModel):
  class Meta:
    verbose_name = "Interactive / Infographic"
    verbose_name_plural = "Interactive / Infographic"
  
  def get_infographics_path(self, filename):
      now = datetime.date
      return os.path.join('uploads/infographics', self.slug, filename)
  
  def get_thumbnail_path(self, filename):
      now = datetime.date
      return os.path.join('uploads/infographics/thumbnails', self.slug, filename)
    
  creation_date = models.DateField(auto_now_add=True)
  last_modified = models.DateField(auto_now=True)
  name = models.CharField(max_length=200, unique=True)
  slug = models.SlugField()
  category = models.ForeignKey('Category', blank=True, null=True)
  tag = models.ManyToManyField(Tag, verbose_name="Tags",blank=True, null=True)
  thumbnail = models.FileField(upload_to=get_thumbnail_path)
  
  translations = TranslatedFields(
    headline = models.CharField(max_length=255, verbose_name=u'* Title/Headline'),
    subheadline = models.CharField(max_length=255, blank=True, null=True, verbose_name=u'* Subheadline'),
    description = models.TextField(verbose_name=u'* Description'),
    single_line_description = models.CharField(max_length=300, blank=True, null=True, verbose_name=u'* Single Line Description (Optional)'),
    infographic_files = models.FileField(upload_to=get_infographics_path, storage=ZipStorage, verbose_name=u"* Interactive's Files (zip file)")
  )
  
  def __unicode__(self):
    return self.name
  
  @staticmethod
  def autocomplete_search_fields():
    return ("id__iexact", "name__icontains",)
  
class StoryPage(TranslatableModel):
  creation_date = models.DateField(auto_now_add=True)
  last_modified = models.DateField(auto_now=True)
  name = models.CharField(max_length=200)
  slug = models.SlugField()
  category = models.ForeignKey('Category', blank=True, null=True)
  tags = models.ManyToManyField(Tag, verbose_name="Tags",blank=True, null=True)
  latitude = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
  longitude = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
  video = models.ForeignKey(Video, verbose_name=u'Story Video')
  related_stories = models.ManyToManyField('StoryPage', verbose_name=u'Related Stories')
  interactives = models.ManyToManyField(Interactive, verbose_name=u'Interactive or Infographic')
  
  translations = common_translated_fields()
    
  def __unicode__(self):
    return self.name
  
  @staticmethod
  def autocomplete_search_fields():
    return ("id__iexact", "name__icontains",)
  
class FeaturedStory(models.Model):
  class Meta:
    verbose_name = 'Featured Story'
    verbose_name_plural = 'Featured Stories'
  name = models.CharField(max_length=100, verbose_name=u'Featured Story Collection Name')
  
class FeaturedStoryItem(models.Model):
  featured_story = models.ForeignKey(FeaturedStory)
  page = models.ForeignKey(StoryPage)
  position = models.PositiveIntegerField("Position")
  
  class Meta:
    ordering = ['position']
  
class Menu(models.Model):
  name = models.CharField(max_length=100)
  
  def __unicode__(self):
    return self.name
 
class MenuItem(models.Model):
  menu = models.ForeignKey(Menu)
  name = models.CharField(max_length=100)
  name_es = models.CharField(max_length=100, verbose_name=u'Spanish Name')
  url = models.CharField(max_length=100)
  page = models.ForeignKey(StoryPage, verbose_name=u'Story Page')
  position = models.PositiveSmallIntegerField("Position")
  
  def __unicode__(self):
    self.name
  
  class Meta:
    ordering = ['position']
  
  
  

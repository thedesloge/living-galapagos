import os
import zipfile
import datetime
from django.db import models
from multilingual_model.models import MultilingualModel, MultilingualTranslation
from livinggalapagos.story_database.zipstorage import ZipStorage
from django.core.files.storage import FileSystemStorage
from django.template.defaultfilters import slugify


# Create your models here.
class Site(models.Model):
  domain = models.CharField(max_length=200, unique=True)
  
  def __unicode__(self):
    return self.domain

class Resources(models.Model):
  class Meta:
    verbose_name = "Resource"
    verbose_name_plural = "Resources"

  name = models.CharField(max_length=100)
  slug = models.SlugField()
  resource_image = models.FileField(upload_to="uploads/resource-images")  
  url = models.URLField(blank=True, null=True)

  def __unicode__(self):
    return self.name

#Start category model
class Category(models.Model):
  class Meta:
    verbose_name = 'Category'
    verbose_name_plural = 'Categories'

  name = models.CharField(max_length=200)
  slug = models.SlugField()

  def __unicode__(self):
    return "Category: " + self.name

class Category_Translation(MultilingualTranslation):
  class Meta:
    unique_together = ('parent', 'language_code')

  parent = models.ForeignKey('Category', related_name='translations')
  translation = models.CharField(max_length=100)

class Background_Video(models.Model):
  class Meta:
    verbose_name = "Background Video"
    verbose_name_plural = "Background Videos"

  name = models.CharField(max_length=100)
  slug = models.SlugField()
  category = models.ForeignKey('Category')
  h264_background = models.FileField(upload_to="uploads/background-video/h264")
  ogg_background = models.FileField(upload_to="uploads/background-video/ogg")
  jpg_background = models.FileField(upload_to="uploads/background-video/jpg")

  def __unicode__(self):
    return self.name

#Start Tag model
class Tag(models.Model):
  name = models.CharField(max_length=100)
  slug = models.SlugField()
  
  def __unicode__(self):
    return "Tag: " + self.name

class Tag_Translation(MultilingualTranslation):
  class Meta:
    unique_together = ('parent', 'language_code')
  
  parent = models.ForeignKey('Tag', related_name='translations')
  translation = models.CharField(max_length=100)


class Video(models.Model):

  creation_date = models.DateField(auto_now_add=True)
  last_modified = models.DateField(auto_now=True)
  name = models.CharField(max_length=200, unique=True)
  slug = models.SlugField()
  category = models.ForeignKey('Category')
  title = models.CharField(max_length=100, blank=True, null=True)
  description = models.TextField(blank=True, null=True)
  vimeo_id = models.IntegerField()
  thumbnail = models.FileField(upload_to='uploads/video/thumbnails/%Y/%m/%d', blank=True, null=True)
  related_content_thumbnail = models.FileField(upload_to='uploads/video/related_thumbs/%Y/%m/%d', blank=True, null=True)  
  tags = models.ManyToManyField(Tag, verbose_name="Tags",blank=True, null=True)
  latitude = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
  longitude = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)

  def __unicode__(self):
    return self.name

class Poster_Frame(models.Model):
  class Meta:
    verbose_name = "Poster Frame"
    verbose_name_plural = "Poster Frames"

  name = models.CharField(max_length=200, unique=True)
  slug = models.SlugField()
  poster_frame = models.FileField(upload_to='uploads/posterframes')
  
  def __unicode__(self):
    return self.name

#Photo and Photo Gallery Begin
class Photo(models.Model):
  
  creation_date = models.DateField(auto_now_add=True)
  last_modified = models.DateField(auto_now=True)
  name = models.CharField(max_length=200, unique=True)
  slug = models.SlugField()
  category = models.ForeignKey('Category', blank=True, null=True)
  photo = models.FileField(upload_to='uploads/photos/%Y/%m/%d')
  tags = models.ManyToManyField(Tag, verbose_name="Tags",blank=True, null=True)
  latitude = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
  longitude = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)

  def __unicode__(self):
    return self.name  

class Photo_Translation(MultilingualTranslation):
  class Meta:
    unique_together = ('parent', 'language_code')
  
  parent = models.ForeignKey(Photo)
  caption = models.TextField()

class Photo_Gallery(models.Model):
  class Meta:
    verbose_name = "Photo Gallery"
    verbose_name_plural = "Photo Galleries"  

  creation_date = models.DateField(auto_now_add=True)
  last_modified = models.DateField(auto_now=True)
  name = models.CharField(max_length=200, unique=True)
  slug = models.SlugField()
  thumbnail = models.FileField(upload_to='uploads/photo_gallery/thumbnails')
  category = models.ForeignKey('Category', blank=True, null=True)
  photos = models.ManyToManyField(Photo, verbose_name="Gallery Photos")
  tag = models.ManyToManyField(Tag, verbose_name="Tags",blank=True, null=True)  
  latitude = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
  longitude = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)

  def __unicode__(self):
    return self.name

class Photo_Gallery_Translation(MultilingualTranslation):
  class Meta:
    unique_together = ('parent', 'language_code')

  parent = models.ForeignKey('Photo_Gallery', related_name='translations')
  title = models.CharField(max_length=200)
  description = models.TextField()
#End Photo and Photo Gallery

#Infographic Content Fields
class Infographic(models.Model):
  class Meta:
    verbose_name = "Infographic"
    verbose_name_plural = "Infographics"

  creation_date = models.DateField(auto_now_add=True)
  last_modified = models.DateField(auto_now=True)
  name = models.CharField(max_length=200, unique=True)
  slug = models.SlugField()
  category = models.ForeignKey('Category', blank=True, null=True)
  tag = models.ManyToManyField(Tag, verbose_name="Tags",blank=True, null=True)
  latitude = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
  longitude = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
  def __unicode__(self):
    return self.name


class Infographic_Translation(MultilingualTranslation):
  class Meta:
    unique_together = ('parent', 'language_code')

  def get_infographics_path(self, filename):
      now = datetime.date
      return os.path.join('uploads/infographics', self.slug, filename)
  
  def get_thumbnail_path(self, filename):
      now = datetime.date
      return os.path.join('uploads/infographics/thumbnails', self.slug, filename)

  parent = models.ForeignKey('Infographic', related_name='translations')
  title = models.CharField(max_length=200)
  slug = models.SlugField()
  short_description = models.CharField(max_length=200, blank=True, null=True)
  description = models.TextField(blank=True, null=True)
  thumbnail = models.FileField(upload_to=get_thumbnail_path)
  is_interactive = models.BooleanField()
  infographic_files = models.FileField(upload_to=get_infographics_path, storage=ZipStorage)
  #infographic_package = models.ForeignKey('Infographic_Package')   

 


#End Infographic Fields

#Related Content Fields
class Related_Content(models.Model):
  class Meta:
    verbose_name = "Related Content"
    verbose_name_plural = "Related Content"

  creation_date = models.DateField(auto_now_add=True)
  last_modified = models.DateField(auto_now=True)
  name = models.CharField(max_length=200, unique=True)
  slug = models.SlugField()
  category = models.ForeignKey('Category', blank=True, null=True)
  tag = models.ManyToManyField(Tag, verbose_name="Tags",blank=True, null=True)

  def __unicode__(self):
    return self.name

class Related_Content_Translation(MultilingualTranslation):
  class Meta:
    unique_together = ('parent', 'language_code')

  parent = models.ForeignKey('Related_Content', related_name='translations')
  videos = models.ManyToManyField(Video, verbose_name="Videos",blank=True, null=True)
  infographics = models.ManyToManyField(Infographic, verbose_name="Infographics",blank=True, null=True)
  photo_galleries = models.ManyToManyField(Photo_Gallery, verbose_name="Photo Galleries",blank=True, null=True) 
  
#End Related Content

class Story(models.Model):
  class Meta:
    verbose_name_plural = "Story"

  creation_date = models.DateField(auto_now_add=True)
  last_modified = models.DateField(auto_now=True)
  menu_order = models.IntegerField(default=0, blank=True)
  site = models.ForeignKey(Site)
  name = models.CharField(max_length=200)
  slug = models.SlugField()
  category = models.ForeignKey('Category', blank=True, null=True)
  tags = models.ManyToManyField(Tag, verbose_name="Tags",blank=True, null=True)
  latitude = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
  longitude = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)

  def __unicode__(self):
    return self.name 

class Story_Translation(MultilingualTranslation):
  class Meta:
	unique_together = ('parent', 'language_code')
  
  parent = models.ForeignKey('Story', related_name='translations')

  headline = models.CharField(max_length=300 )
  subheadline = models.CharField(max_length=300)
  single_line_description = models.CharField(max_length=300)
  description = models.TextField()
  quote = models.TextField(blank=True, null=True)
  quote_attribution = models.TextField(blank=True, null=True)
  poster_frame = models.ForeignKey(Poster_Frame, blank=True, null=True)
  featured_video = models.ForeignKey(Video, blank=True, null=True)
  related_content = models.ForeignKey(Related_Content, blank=True, null=True) 
  
  def __unicode__(self):
    return "Story Translation"

class Research(models.Model):
  class Meta:
    verbose_name_plural = "Research"
    
  name = models.CharField(max_length=30)
  slug = models.SlugField()
  category = models.ForeignKey('Category', blank=True, null=True)

  def __unicode__(self):
    return self.name
  
class Research_Translation(MultilingualTranslation):
  class Meta:
    unique_together = ('parent', 'language_code')

  parent = models.ForeignKey('Research', related_name='translations')
  title = models.CharField(max_length=100)
  institute = models.CharField(max_length=100)
  short_description = models.TextField()
  url = models.URLField(blank=True, null=True)

class Featured_Story(models.Model):
  class Meta:
    verbose_name = "Featured Story"
    verbose_name_plural = "Featured Stories"
  
  name = models.CharField(max_length=50)
  slug = models.SlugField()
  story = models.ForeignKey('Story', help_text="This is the Featured story for the website", unique=True)

class About_Page(models.Model):
  class Meta:
    verbose_name_plural = "About Page"

  creation_date = models.DateField(auto_now_add=True)
  last_modified = models.DateField(auto_now=True)
  site = models.ForeignKey(Site)
  name = models.CharField(max_length=200)
  slug = models.SlugField()

  def __unicode__(self):
    return self.name 

class About_Page_Translation(MultilingualTranslation):
  class Meta:
	unique_together = ('parent', 'language_code')
  
  parent = models.ForeignKey('About_Page', related_name='translations')

  headline = models.CharField(max_length=300 )
  subheadline = models.CharField(max_length=300)
  about_text = models.TextField()
  quote = models.TextField(blank=True, null=True)
  quote_attribution = models.TextField(blank=True, null=True)
  featured_video = models.ForeignKey(Video, blank=True, null=True)
  related_content = models.ForeignKey(Related_Content, blank=True, null=True) 
  
  def __unicode__(self):
    return "About Page Translation"

class Title_Card(models.Model):
    class Meta:
        verbose_name = "Title Card"
        verbose_name_plural = "Title Cards"
    
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    story = models.ForeignKey('Story')

    def __unicode__(self):
      return self.name
    
class Title_Card_Translation(MultilingualTranslation):
    class Meta:
        unique_together = ('parent', 'language_code')
        
    parent = models.ForeignKey('Title_Card', related_name='translation')
    title_card = models.FileField(upload_to="uploads/title-cards/%Y/%m/%d")


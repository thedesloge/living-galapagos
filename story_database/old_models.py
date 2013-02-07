from django.db import models

# Create your models here.
class Site(models.Model):
  domain = models.CharField(max_length=200)
  
  def __unicode__(self):
    return self.domain
  
class Story(models.Model):
  site = models.ForeignKey('Site')
  name = models.CharField(max_length=200)
  
  def __unicode__(self):
    return self.name
  
class StoryVideo(models.Model):
  title = models.CharField(max_length=200)
  single_line_summary = models.CharField(max_length=200)
  multiline_summary = models.TextField()
  vimeo_id = models.CharField(max_length=200)
  story = models.ForeignKey(Story)

class PhotoGallery(models.Model):
  title = models.CharField(max_length=200)
  summary = models.TextField()
  story = models.ForeignKey(Story)
  
  def __unicode__(self):
    return self.title

class Photo(models.Model):
  photo_gallery = models.ForeignKey(PhotoGallery)
  name = models.CharField(max_length=200)


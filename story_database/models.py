import os
import zipfile
import datetime
from django.db import models
from hvad.models import TranslatableModel, TranslatedFields
from story_database.zipstorage import ZipStorage
from django.core.files.storage import FileSystemStorage
from django.template.defaultfilters import slugify

def common_translated_fields():
      return TranslatedFields(
                              headline = models.CharField(max_length=255, verbose_name=u'* Title/Headline'),
                              subheadline = models.CharField(max_length=255, blank=True, null=True, verbose_name=u'* Subheadline (Optional)'),
                              description = models.TextField(verbose_name=u'* Description'),
                              single_line_description = models.CharField(max_length=300, blank=True, null=True, verbose_name=u'* Single Line Description (Optional)'),
                              quote = models.TextField(blank=True, null=True, verbose_name=u'* Quote (Optional)'),
                              quote_attribution = models.TextField(blank=True, null=True, verbose_name=u'* Attribution (Optional)'),
      )

class Role(models.Model):
    title = models.CharField(max_length=100)
    
    def __unicode__(self):
        self.title

class Credit(TranslatableModel):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    role = models.ManyToManyField(Role)
    
    translations = TranslatedFields(
        bio = models.TextField(verbose_name="* Bio | About (Brief)"),
    )
    
    def __unicode__(self):
        return self.first_name, " ", self.last_name


class Category(TranslatableModel):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField()
    
    translations = TranslatedFields(
                                    translation = models.CharField(max_length=100)
    )
    
    def __unicode__(self):
      return "Category: " + self.name
    
    @staticmethod
    def autocomplete_search_fields():
      return ("id__iexact", "name__icontains",)
  
class Tag(TranslatableModel):
    name = models.CharField(max_length=100, unique=True)
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
    slug = models.SlugField()
    author = models.ForeignKey(Credit, null=True, blank=True)
    category = models.ForeignKey('Category', blank=True, null=True)
    thumbnail = models.FileField(upload_to='uploads/video/thumbnails/%Y/%m/%d', blank=True, null=True, verbose_name=u'Thumbnail (Optional)')
    
    translations = TranslatedFields(
        headline = models.CharField(max_length=255, verbose_name=u'* Title/Headline'),
        subheadline = models.CharField(max_length=255, blank=True, null=True, verbose_name=u'* Subheadline'),
        description = models.TextField(verbose_name=u'* Description'),
        single_line_description = models.CharField(max_length=300, blank=True, null=True, verbose_name=u'* Single Line Description (Optional)'),
        vimeo_id = models.IntegerField(verbose_name=u'* Vimeo ID'),
        poster_frame = models.ForeignKey('PosterFrame', blank=True, null=True, verbose_name="* Poster Frame"),
        title_card = models.FileField(upload_to='uploads/video/title-card/%Y/%m/%d', blank=True, null=True, verbose_name=u'Title Card')
    )
    
    def thumbnail_image(self):
        if self.thumbnail:
            return '<img src="/media/%s" width="200px"/>' % self.poster_frame.url
        else:
            return 'None'
    thumbnail_image.allow_tags = True
    
    def __unicode__(self):
      return self.name
    
    @staticmethod
    def autocomplete_search_fields():
      return ("id__iexact", "name__icontains",)

class PosterFrame(models.Model):
    class Meta:
        verbose_name = "Poster Frame | Title Card"
        verbose_name_plural = "Poster Frames | Title Cards"
    
    def get_poster_frame_path(self, filename):
        now = datetime.date
        return os.path.join('uploads/posterframes/%Y', self.slug, filename)
    
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField()
    is_spanish = models.BooleanField(blank=True, default=False, verbose_name="Is Spanish Translation")
    poster_frame = models.FileField(upload_to=get_poster_frame_path)
    
    def poster_frame_image(self):
        return '<img src="/media/%s" width="200px"/>' % self.poster_frame.url
    poster_frame_image.allow_tags = True
    
    def __unicode__(self):
        return self.name
    
    @staticmethod
    def autocomplete_search_fields():
        return ("id__iexact", "name__icontains",)
 
class Interactive(models.Model):
    class Meta:
        verbose_name = "Interactive | Infographic"
        verbose_name_plural = "Interactives | Infographics"
    
    def get_infographics_path(self, filename):
        now = datetime.date
        return os.path.join('uploads/infographics', self.slug, filename)
    
    def get_thumbnail_path(self, filename):
        now = datetime.date
        return os.path.join('uploads/infographics/thumbnails', self.slug, filename)
      
    creation_date = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)
    name = models.CharField(max_length=200, unique=True)
    author = models.ManyToManyField(Credit, blank=True, null=True)
    slug = models.SlugField()
    category = models.ForeignKey('Category', blank=True, null=True)
    tag = models.ManyToManyField(Tag, verbose_name="Tags",blank=True, null=True)
    is_spanish = models.BooleanField(blank=True, default=False, verbose_name="Is Spanish Translation")
    thumbnail = models.FileField(upload_to=get_thumbnail_path)
    headline = models.CharField(max_length=255, verbose_name=u'Title/Headline')
    subheadline = models.CharField(max_length=255, blank=True, null=True, verbose_name=u'Subheadline')
    description = models.TextField(verbose_name=u'Description')
    single_line_description = models.CharField(max_length=300, blank=True, null=True, verbose_name=u'* Single Line Description (Optional)'),
    infographic_files = models.FileField(upload_to=get_infographics_path, storage=ZipStorage, verbose_name=u"* Interactive's Files (zip file)", null=True)
    poster_frame = models.ForeignKey('PosterFrame', blank=True, null=True, verbose_name=u"Interactive Posterframe (used for article page, width 780)")
    
    def __unicode__(self):
        return self.name
    
    def thumbnail_image(self):
        if self.thumbnail:
            return '<img src="/media/%s" width="200px"/>' % self.thumbnail.url
        else:
            return 'None'
    thumbnail_image.allow_tags = True
    
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
    video = models.ForeignKey(Video, verbose_name=u'Story Video', blank=True, null=True)
    related_stories = models.ManyToManyField('StoryPage', verbose_name=u'Related Stories', blank=True, null=True)
    interactives = models.ManyToManyField(Interactive, verbose_name=u'Interactive or Infographic', blank=True, null=True)
    thumbnail = models.FileField(upload_to='uploads/story/thumbnail/%Y/%m/%d', blank=True, null=True)
    
    translations = common_translated_fields()
      
    def __unicode__(self):
        return self.name
    
    @staticmethod
    def autocomplete_search_fields():
        return ("id__iexact", "name__icontains",)
      

  
class FeaturedStory(models.Model):
    class Meta:
        verbose_name = "Featured Story"
        verbose_name_plural = "Featured Stories"
        
    name = models.CharField(max_length=100)
  
    def __unicode__(self):
        return self.name
 
class FeaturedStoryItem(models.Model):
    menu = models.ForeignKey(FeaturedStory)
    page = models.ForeignKey(StoryPage, verbose_name=u'Story Page')
    position = models.PositiveSmallIntegerField("Position")
    
    def __unicode__(self):
        return "Featured Story Item for ", self.menu.name, " with page: ", self.page.name
    
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
    
class BackgroundVideo(models.Model):
    class Meta:
        verbose_name = "Background Video"
        verbose_name_plural = "Background Videos"
    
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    category = models.ForeignKey('Category')
    story_page = models.ForeignKey('StoryPage', blank=True, null=True)
    h264_background = models.FileField(upload_to="uploads/background-video/h264", blank=True, null=True)
    ogg_background = models.FileField(upload_to="uploads/background-video/ogg", blank=True, null=True)
    jpg_background = models.FileField(upload_to="uploads/background-video/jpg", blank=True, null=True)
    
    def fallback_image(self):
        if self.jpg_background:
            return '<img src="/media/%s" width="200px"/>' % self.jpg_background.url
        else:
            return 'None'
    fallback_image.allow_tags = True
        
    def __unicode__(self):
        return self.name

class ArticleChapter(TranslatableModel):
  creation_date = models.DateField(auto_now_add=True)
  last_modified = models.DateField(auto_now=True)
  name = models.CharField(max_length=200)
  slug = models.SlugField()
  related_stories = models.ManyToManyField('ArticlePage', verbose_name=u'Related Stories', blank=True, null=True)
  videos = models.ManyToManyField(Video, verbose_name=u'Related Videos', blank=True, null=True)
  pano_head = models.FileField(upload_to='uploads/article/pano_head/%Y/%m/%d', blank=True, null=True, verbose_name=u'Chapter Heading Pano Image')
  translations = TranslatedFields(
                  headline = models.CharField(max_length=255, verbose_name=u'* Title/Headline'),
                  subheadline = models.CharField(max_length=255, blank=True, null=True, verbose_name=u'* Subheadline (Optional)'),
                  body_text = models.TextField(verbose_name=u'* Description'),
                  quote = models.TextField(blank=True, null=True, verbose_name=u'* Quote (Optional)'),
                  quote_attribution = models.TextField(blank=True, null=True, verbose_name=u'* Attribution (Optional)'),
                  interactives = models.ManyToManyField(Interactive, verbose_name=u'Interactive or Infographic', blank=True, null=True),
  )
    
  def __unicode__(self):
      return self.name
  
  @staticmethod
  def autocomplete_search_fields():
      return ("id__iexact", "name__icontains",)

class ArticlePage(TranslatableModel):
  creation_date = models.DateField(auto_now_add=True)
  last_modified = models.DateField(auto_now=True)
  name = models.CharField(max_length=200)
  slug = models.SlugField()
  article_chapter = models.ManyToManyField(ArticleChapter, blank=True, null=True)
  thumbnail = models.FileField(upload_to='uploads/article/thumbnail/%Y/%m/%d', blank=True, null=True)
    
  translation = TranslatedFields(
                title = models.CharField(max_length=255, verbose_name=u'* Title/Headline')
  )
  def __unicode__(self):
      return self.name
  
  @staticmethod
  def autocomplete_search_fields():
      return ("id__iexact", "name__icontains",)





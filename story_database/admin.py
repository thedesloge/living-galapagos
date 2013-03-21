from django.contrib import admin
from django import forms
from story_database.models import *
from hvad.admin import TranslatableAdmin
from hvad.forms import TranslatableModelForm

class StoryPageAdmin(TranslatableAdmin):
  model = StoryPage
  list_display = ('name', 'video', 'category', 'all_translations',)
  list_display_links = ('name', 'video',)
  list_filter = ('category', 'tags', 'creation_date', 'last_modified')
  filter_horizontal = ('tags', 'related_stories', 'interactives')
  raw_id_fields = ('video',)
  autocomplete_lookup_fields = {
    'fk': ['video'],
  }
  search_fields  = ['name']
  prepopulated_fields = {"slug": ("name",)}
  
  

class InteractiveAdmin(admin.ModelAdmin):
  model = Interactive
  list_display = ('name', 'thumbnail_image', 'is_spanish',)
  list_display_links = ('name',)
  list_filter = ('category', 'tag', 'creation_date', 'last_modified', 'is_spanish')
  filter_horizontal = ('tag',)
  raw_id_fields = ('category',)
  prepopulated_fields = {"slug": ("name",)}
  autocomplete_lookup_fields = {
    'fk': ['category']
  }
  search_fields = ['name']
        
    
class VideoAdmin(TranslatableAdmin):
  model = Video
  list_filter = ('creation_date', 'last_modified', 'category')
  list_display = ('name', 'thumbnail', 'all_translations', 'author')
  search_fields = ['name']
  prepopulated_fields = {"slug": ("name",)}
  raw_id_fields = ('category', 'author')
  autocomplete_lookup_fields = {
    'fk': ['category', 'author']
  }
  
  
class ItemInline(admin.TabularInline):
  model = MenuItem
  fields = ('name','name_es', 'page', 'position')
  raw_id_fields = ('page',)
  sort_field_name = "position"
  
  autocomplete_lookup_fields = {
    'fk': ['page'],
  }

class FeaturedStoryItemInline(admin.TabularInline):
  model = FeaturedStoryItem
  fields = ('page', 'position')
  raw_id_fields = ('page',)
  sort_field_name = "position"
  
  autocomplete_lookup_fields = {
    'fk': ['page'],
  }
  
class PosterFrameAdmin(admin.ModelAdmin):
    model = PosterFrame
    list_display = ('name', 'poster_frame_image','is_spanish')
    search_fields = ['name']
    list_filter = ('is_spanish',)
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Menu,
                  inlines = [ItemInline],
)

class TagAdmin(TranslatableAdmin):
    model = Tag
    list_display = ('name', 'all_translations',)
    prepopulated_fields = {'slug':('name',)}
    search_fields = ['name']
    
class CategoryAdmin(TranslatableAdmin):
    model = Category
    list_display = ('name', 'all_translations')
    prepopulated_fields = {'slug':('name',)}
    search_fields = ['name']
    
class BackgroundVideoAdmin(admin.ModelAdmin):
    model = BackgroundVideo
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'category', 'story_page', 'h264_background', 'ogg_background', 'fallback_image')
    search_fields= ['name']
    raw_id_fields = ('story_page','category',)
    autocomplete_lookup_fields = {
    'fk': ['story_page', 'category'],
  }
    
class CreditAdmin(TranslatableAdmin):
    model = Credit
    search_fields = ['name']
       
admin.site.register(FeaturedStory,
                    inlines = [FeaturedStoryItemInline],
                    )
admin.site.register(StoryPage, StoryPageAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Interactive, InteractiveAdmin)
admin.site.register(PosterFrame, PosterFrameAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(BackgroundVideo, BackgroundVideoAdmin)
admin.site.register(Role)
admin.site.register(Credit, CreditAdmin)


from django.contrib import admin
from django import forms
from language_test.models import *
from hvad.admin import TranslatableAdmin

class StoryPageAdmin(TranslatableAdmin):
  model = StoryPage
  list_display = ('name', 'video')
  list_display_links = ('name', 'video',)
  list_filter = ('category', 'tags', 'creation_date', 'last_modified')
  filter_horizontal = ('tags', 'related_stories', 'interactives')
  raw_id_fields = ('video',)
  autocomplete_lookup_fields = {
    'fk': ['video'],
  }
  search_fields  = ['name']

class InteractiveAdmin(TranslatableAdmin):
  model = Interactive
  list_display = ('name',)
  list_display_links = ('name',)
  list_filter = ('category', 'tag', 'creation_date', 'last_modified')
  filter_horizontal = ('tag',)
  raw_id_fields = ('category',)
  autocomplete_lookup_fields = {
    'fk': ['category']
  }
  search_fields = ['name']
  
class VideoAdmin(TranslatableAdmin):
  model = Video
  list_filter = ('creation_date', 'last_modified', 'category')
  search_fields = ['name']
  
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
  
  auto_complete_name = {
    'fk': ['page'],
  }

admin.site.register(Menu,
                  inlines = [ItemInline],
)
admin.site.register(FeaturedStory,
                    inlines = [FeaturedStoryItemInline],
                    )
admin.site.register(StoryPage, StoryPageAdmin) 
admin.site.register(Video, VideoAdmin)
admin.site.register(Interactive, InteractiveAdmin)


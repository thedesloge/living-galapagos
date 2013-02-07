from livinggalapagos.story_database.models import * 
from django.contrib import admin
from multilingual_model.admin import TranslationInline

class CategoryTranslationInline(TranslationInline):
  model = Category_Translation

class CategoryAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug":("name",)}
  list_display = ['name']
  inlines = [CategoryTranslationInline]

class TagTranslationInline(TranslationInline):
  model = Tag_Translation

class TagAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug":("name",)}
  list_display = ['name'];
  inlines = [TagTranslationInline]

class PosterFrameAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug":("name",)}
  list_display = ['name']

class RelatedContentTranslationInline(TranslationInline):
  model = Related_Content_Translation

class RelatedContentAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug":("name",)}
  list_display = ['name']
  inlines = [RelatedContentTranslationInline]

class InfographicTranslationInline(TranslationInline):
  prepopulated_fields = {"slug":("title",)}
  model = Infographic_Translation

class InfographicAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug":("name",)}
  list_display = ['name']
  inlines = [InfographicTranslationInline]

class PhotoGalleryTranslationInline(TranslationInline):
  model = Photo_Gallery_Translation

class PhotoGalleryAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug":("name",)}
  list_display = ['name']
  inlines = [PhotoGalleryTranslationInline]

class PhotoTranslationInline(TranslationInline):
  model = Photo_Translation

class PhotoAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug":("name",)}
  list_display = ['name']
  inlines = [PhotoTranslationInline]

class StoryTranslationInline(TranslationInline):
  model = Story_Translation
  fieldsets = [
       (None, {'fields': ['language_code']}),
       ('Translation', {'fields' : ['headline', 'subheadline', 'single_line_description', 'description', 'quote', 'quote_attribution','poster_frame','featured_video', 'related_content'], 'classes' : ['collapse']})] 

class StoryAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug":("name",)}
  list_display = ['name', 'creation_date', 'last_modified', 'menu_order']
  search_fields = ['name']
  list_filter = ['creation_date']
  inlines = [StoryTranslationInline]

class ResearchTranslation(TranslationInline):
  model = Research_Translation

class ResearchAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug":("name",)}
  list_display = ['name']
  inlines = [ResearchTranslation]

class VideoAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug":("name",)}

class AboutPageTranslationInline(TranslationInline):
  model = About_Page_Translation

class AboutPageAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("name",)}
    inlines = [AboutPageTranslationInline]
    
class FeaturedStoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("name",)}
    
class BackgroundVideoAdmin(admin.ModelAdmin):
    prepopulated_field = {"slug":("name",)}
    
    
class TitleCardTranslationInline(TranslationInline):
  model = Title_Card_Translation 

class TitleCardAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug":("name",)}
  inlines = [TitleCardTranslationInline]
    
admin.site.register(Site)
admin.site.register(Story, StoryAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Infographic, InfographicAdmin)
#admin.site.register(Photo, PhotoAdmin)
#admin.site.register(Photo_Gallery, PhotoGalleryAdmin)
admin.site.register(Related_Content, RelatedContentAdmin)
admin.site.register(Poster_Frame, PosterFrameAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Resources)
admin.site.register(Featured_Story, FeaturedStoryAdmin)
admin.site.register(Research, ResearchAdmin)
admin.site.register(Background_Video, BackgroundVideoAdmin)
admin.site.register(About_Page, AboutPageAdmin)
admin.site.register(Title_Card, TitleCardAdmin)

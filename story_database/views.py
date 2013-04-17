# Create your views here.
from django.http import Http404
from django.shortcuts import *
from story_database.models import *
from pprint import PrettyPrinter
from django import forms
from haystack.query import SearchQuerySet
from django.conf import settings

def home(request, language_code='en'):
  return render_to_response(
            'story_database/home.html',
            getLanguageForStory( getFeaturedStoryPage(), language_code, request, True ),
            context_instance=RequestContext(request)
        )

def article_story_page(request, article_slug, language_code='en'):
  return render_to_response(
            'story_database/article.html',
            getLanguageForArticle( get_article_by_slug(request, article_slug), language_code, request ),
            context_instance=RequestContext(request)
        )

def learn(request):
  return render_to_response(
            'story_database/learn.html',
            {'language':'en', 'menu': get_menu('en')},
            context_instance=RequestContext(request)
        )

def featured_story_page(request, story_slug, language_code='en'):
  return render_to_response(
            'story_database/featured.html',
            getLanguageForStory( getStoryBySlug(request, story_slug), language_code, request, False ),
            context_instance=RequestContext(request)
        )

def about(request, language_code='en'):
  return render_to_response(
            'story_database/about.html',
            getLanguageForStory( getStoryBySlug(request, 'about'), language_code, request, False ),
            context_instance=RequestContext(request)
        )
  

def search(request, language_code='en'):
  if request.method == 'POST':
    form = SearchForm(request.POST)
    if form.is_valid():
        filtered_list = {}
        search = form.cleaned_data['search']
        
        story_query_set = SearchQuerySet().filter(text=search)
        print "Got ", story_query_set.filter(language_code='en').count(), " stories"
        filtered_list['story_list'] = {}
        background_vid = {}
        
        return render_to_response('story_database/search.html', {'form':form, "filtered_list":filtered_list,"background_video":background_vid, "language":language_code}, context_instance=RequestContext(request))
    else:    
      return render_to_response('story_database/search.html', {'form':form, "language":language_code}, context_instance=RequestContext(request))
  else:  
    form = SearchForm(initial={'category_land':True, 'category_sea':True, 'category_archive':True})
    all_stories = StoryPageTranslation.objects.filter(language_code=language_code)
    story_list = {}
    
    temp_list = {}
    for story in all_stories:
        if story.master.thumbnail:
            temp_list['thumbnail'] = story.master.thumbnail.url
            
        temp_list['slug'] = story.master.slug
        temp_list['headline'] = story.headline
        temp_list['single_line_description'] = story.single_line_description 
    story_list['story_list'] = temp_list
    
    background_vid = {}
    #try:
    #    cat = Category.objects.get(slug='category-sea');
    #    background_vid = Background_Video.objects.get(category=cat)
    #except Background_Video.DoesNotExist:  
    #    pass
    
    return render_to_response('story_database/search.html', {'form':form, "filtered_list":story_list, "background_video":background_vid , "language":language_code}, context_instance=RequestContext(request))

def search_map(request, language_code='en'):
  if request.method == 'POST':
    form = SearchForm(request.POST)
    if form.is_valid():
        filtered_list = {}
        search = form.cleaned_data['search']
        
        storyList = {}
        tags = Tag.objects.filter(name__in=form.cleaned_data['tags']).order_by('name')
        
        if (form.cleaned_data['category_sea'] and form.cleaned_data['category_land']):
            if tags:
                storyList = Story.objects.filter(tags__in=tags)
            else:
                storyList = Story.objects.all()
            
        elif form.cleaned_data['category_sea']:
            cat = Category.objects.get(slug='category-sea')
            if tags:
                storyList = Story.objects.filter(category=cat, tags__in=tags)
            else:
                storyList = Story.objects.filter(category=cat)
                
        elif form.cleaned_data['category_land']:
            cat = Category.objects.get(slug='category-land')
            if tags:
                storyList = Story.objects.filter(category=cat, tags__in=tags)
            else:
                storyList = Story.objects.filter(category=cat)
                
        filtered_list['story_list'] = getFilteredCategory(search, language_code, storyList)
        background_vid = {}
        try:
            cat = Category.objects.get(slug='category-sea');
            background_vid = Background_Video.objects.get(category=cat)
        except Background_Video.DoesNotExist:  
            pass
    
        return render_to_response('story_database/search_map.html', {'form':form, "filtered_list":filtered_list, "background_video":background_vid, "language":language_code}, context_instance=RequestContext(request))
    else:    
      return render_to_response('story_database/search_map.html', {'form':form, "language":language_code}, context_instance=RequestContext(request))
  else:  
    form = SearchForm(initial={'category_land':True, 'category_sea':True, 'category_archive':True})
    allStories = Story.objects.all().order_by('menu_order')
    story_list = {}
    story_list['story_list'] = Story_Translation.objects.filter(parent__in=allStories, language_code=language_code)
    background_vid = {}
    try:
        cat = Category.objects.get(slug='category-sea');
        background_vid = Background_Video.objects.get(category=cat)
    except Background_Video.DoesNotExist:  
        pass
    
    return render_to_response('story_database/search_map.html', {'form':form, "filtered_list":story_list, "background_video":background_vid, "language":language_code}, context_instance=RequestContext(request))


#END VIEW HANDLING BEGIN support functions

def getFeaturedStoryPage():
  
  try:
      featured_story_collection = FeaturedStory.objects.get(name="Main Page")
      return featured_story_collection.featuredstoryitem_set.all()[0].page
  except FeaturedStory.DoesNotExist:
      raise Http404
  

def getStoryBySlug(request, storySlug):
  try:
      
    if request.session.get('isECUADOR') == True and storySlug == 'forbidden-refuge':
        raise Http404  

    story = StoryPage.objects.get(slug=storySlug)
    
  except StoryPage.DoesNotExist:
    raise Http404

  return story
  
def get_article_by_slug(request, article_slug):
    
    try:
        article_page = ArticlePage.objects.get(slug=article_slug)
        return article_page
    except ArticlePage.DoesNotExist:
        raise Http404
    

def getLanguageForStory(story, language, request, isFeatured):
  
  template_object = {}
  template_object["is_mobile"] = request.is_mobile
  template_object['menu'] = get_menu(language)
  
  #Story Language Translated items
  try:
      story_translation = story.translations.get(language_code=language)
  except StoryPageTranslation.DoesNotExist:
      raise Http404
  
  template_object['headline'] = story_translation.headline
  template_object['description'] = story_translation.description
  template_object['quote'] = story_translation.quote
  template_object['quote_attribution'] = story_translation.quote_attribution
  
  #Story Page video
  template_object['video'] = buildVideoObject(Video.objects.language(language).get(id=story.video.id))
  #Get Interactives
  template_object['related_content_list'] = getInteractivedForStory(story, language)
  #Story Page Related Stories
  template_object['related_stories'] = {}
  template_object['language'] = language
  #template_object['site_categories'] = Category.objects.all()
  #template_object['stories_in_category'] = getStoriesInCategory(request, story.category, language)
  #template_object['category_sea_stories'] = getStoriesInCategory(request, "category-sea", language)
  #template_object['category_land_stories'] = getStoriesInCategory(request, "category-land", language)
  template_object['english_link'] = getEnglishLink(request) 
  template_object['spanish_link'] = getSpanishLink(request)
  #template_object['resource_list'] = []
  #template_object['research_list'] = []
  template_object['category_header'] = getCategoryHeader(story.story_category_header, language)
  try:
      if isFeatured:
          template_object['background_video'] = BackgroundVideo.objects.get(category=Category.objects.get(name='cover'))
      else:
          template_object['background_video'] = BackgroundVideo.objects.get(category=story.category)
  except BackgroundVideo.DoesNotExist:
    pass
  except Category.DoesNotExist:
    pass

  return template_object

def getCategoryHeader(category_header, language):
  ret_val = {}
  if(category_header):
      ret_val['title'] = category_header.translations.get(language_code=language).category_name
      ret_val['description'] = category_header.translations.get(language_code=language).category_description
      if category_header.background_image:
          ret_val['background_image'] = category_header.background_image.url
  return ret_val
  
def getLanguageForArticle(article, language, request):
    template_object = {}
    template_object["is_mobile"] = request.is_mobile
    template_object['menu'] = get_menu(language)
    template_object['language'] = language
    try:
        chapters = article.article_chapter.all()
        
        chap_obj = []
        for chapter in chapters:
            chap_translation = chapter.translations.get(language_code=language)
            chap={}
            chap['headline'] = chap_translation.headline
            chap['subheadline'] = chap_translation.subheadline
            chap['body_text'] = chap_translation.body_text
            chap['infographics'] = chap_translation.interactives.all()
            chap['quote'] = chap_translation.quote
            chap['quote_attribution'] = chap_translation.quote_attribution
            chap['id'] = chap_translation.id
            videos = []
            translated_videos = chapter.videos.all()
            for vid in translated_videos:
                videos.append(buildVideoObject(vid))
                
            chap['videos'] = videos
            #chap['vimeo_id'] = vid.vimeo_id
        
            
            
            if chapter.pano_head:
                chap['pano_head'] = chapter.pano_head.url
                
            chap_obj.append(chap)
        template_object["chapters"] = chap_obj
        
        try:
          if isFeatured:
              template_object['background_video'] = BackgroundVideo.objects.get(category=Category.objects.get(name='cover'))
          else:
              template_object['background_video'] = BackgroundVideo.objects.get(category=story.category)
        except BackgroundVideo.DoesNotExist:
          pass
        except Category.DoesNotExist:
          pass
    
    except ArticlePage.DoesNotExist:
        pass
    return template_object



def buildVideoObject(video):
    video_obj = {}
    if video.thumbnail:
        video_obj['thumbnail'] = video.thumbnail.url
    
    video_obj['vimeo_id'] = video.vimeo_id
    video_obj['headline'] = video.headline
    video_obj['description'] = video.description
    video_obj['subheadline'] = video.subheadline
    if video.poster_frame:
        video_obj['poster_frame'] = video.poster_frame.poster_frame.url
    video_obj['single_line_description'] = video.single_line_description
    if video.title_card:
        video_obj["title_card"] = video.title_card.url
    
    return video_obj

def getInteractivedForStory(story, language):
    list = story.interactives.all()
    
    interactive_list = []
    for interactive in list:
        if interactive.is_spanish and language == 'es':
            interactive_list.append(interactive)
        elif not interactive.is_spanish and language == 'en': 
            interactive_list.append(interactive)
    
    return interactive_list
    

def getEnglishLink(request):
  if request.path.startswith('/es'):
    return '/en' + request.path[3:]
  elif request.path.startswith('/en'):
    return request.path
  else:
    return '/en' + request.path

def getSpanishLink(request):
  if request.path.startswith('/en'):
    return '/es' + request.path[3:]
  elif request.path.startswith('/es'):
    return request.path
  else:
    return '/es' + request.path


def getStoriesInCategory(request, category, language):
    
    try:
        cat = Category.objects.get(slug=category)
        story_list = cat.storypage_set.all()
        ret_val = []
        for story in story_list:
            story_obj = {}
            story_obj['thumbnail'] = story.thumbnail
            story_obj['slug'] = story.slug
            story_obj['title'] = story.translations.get(language_code=language).headline
            ret_val.append(story_obj)
         
        return  ret_val
         
    except TypeError as inst:
        return {}
    except Category.DoesNotExist:
        return {}
        pass
            
def get_menu(language='en'):
    menu_all = Menu.objects.all(); 
    ret_val = {}
    menu_slides = []
    for index, menu in enumerate(menu_all):
        menu_slide = {}
        try:
            menu_slide['category'] =  menu.category.translations.get(language_code=language).translation
            menu_slide['category_slug'] = menu.category.slug
            menu_slide['menu_item_html'] = build_menu( menu_slide['category_slug'], menu.menuitem_set.all().order_by('-position'), language, index==0 )
            
            menu_slides.append( menu_slide )
        except Category.DoesNotExist:
            raise Http404
        
        
        
    ret_val['menu_slides'] = menu_slides
    
    return ret_val

def build_menu(category, menu_items, language, active=False):
    menu_string = []
    menu_string.append( outer_start_div(category, active) )
    
    build_slides(menu_items, menu_string, language)
    
    menu_string.append( outer_end_div() )
    return ''.join(menu_string)

def build_slides(menu_items, menu_string, language):
    
    if len(menu_items) == 0 :
        return menu_string.append("</div>")
    else:
        slide_items = menu_items[:5]
        menu_string.append( make_slide(slide_items, language) )
        
        items_to_pass = menu_items[5:]
        build_slides(items_to_pass, menu_string, language)
        
def make_slide(slide_items, language):
    slide_html = ['<div>']
    
    make_row(slide_items[:3], slide_html, language)
    make_row(slide_items[2:], slide_html, language)
    
    slide_html.append('</div>')
    
    return ''.join( slide_html )

def make_row(row_items, slide_html, language):
    if len(row_items) == 0:
        return 
    slide_html.append('<div class="row tabs-content-slider-row">')
    
    
    for item in row_items:
        slide_html.append('<div class="tabs-content-link">')
        slide_html.append('<a href="/'+ language + '/' + item.page.slug + '"><img src="' +  item.page.thumbnail.url +'"/>')
        slide_html.append('<div class="tabs-image-caption">')
        slide_html.append('<img src="' + settings.STATIC_URL + 'images/icon.png"/>')
        slide_html.append('<h4>' + item.page.translations.get(language_code=language).headline + '</h4>')
        slide_html.append('<p>' + item.page.translations.get(language_code=language).subheadline + '</p></a>')
        slide_html.append('</div>')
        slide_html.append('</div>')
    
    slide_html.append('</div>')
     
 
def outer_start_div(category, active=False):
    if active:
        return '<li class="active" id="' + category + 'Tab"><div id="' + category + 'ContentSlider">'
    else:
        return '<li id="' + category + 'Tab"><div id="' + category + 'ContentSlider">'  

def outer_end_div():
    return '' 

def getFilteredCategory(search, language_code, storyList):
    storyTrans = Story_Translation.objects.filter(language_code=language_code, parent__in=storyList)
    filteredStories = []
    filteredStories = storyTrans.filter(description__contains=search)
    return filteredStories  
  
  
class SearchForm(forms.Form):
  TAGS=(
    ('Tag1', 'Tag1'),
    ('Tag2', 'Tag2'),      
  )
  
  def getTags():
      return Tag.objects.distinct('name').values_list('name', 'name').order_by('name')
  
  YEAR_CHOICES = (
    ('2012', '2012'),
  )
  
  search = forms.CharField(required=False)
  category_land = forms.BooleanField(required=False, initial=True)
  category_sea = forms.BooleanField(required=False, initial=True)
  category_archive = forms.BooleanField(required=False, initial=True)
  tags = forms.MultipleChoiceField(choices=getTags(), required=False)
  

# Create your views here.
from django.http import Http404
from django.shortcuts import *
from story_database.models import *
from pprint import PrettyPrinter
from django import forms


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

def learn(request, story_slug, language_code='en'):
  return render_to_response(
            'story_database/learn.html',
            getLanguageForStory( getStoryBySlug(request, story_slug), language_code, request, False ),
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
        
        storyList = {}
        tags = Tag.objects.filter(name__in=form.cleaned_data['tags'])
        
        if (form.cleaned_data['category_sea'] and form.cleaned_data['category_land'] and form.cleaned_data['category_archive']):
            if tags:
                storyList = Story.objects.filter(tags__in=tags).order_by('menu_order')
            else:
                storyList = Story.objects.all()
            
        elif form.cleaned_data['category_sea']:
            cat = Category.objects.get(slug='category-sea')
            if tags:
                storyList = Story.objects.filter(category=cat, tags__in=tags).order_by('menu_order')
            else:
                storyList = Story.objects.filter(category=cat).order_by('menu_order')
                
        elif form.cleaned_data['category_land']:
            cat = Category.objects.get(slug='category-land')
            if tags:
                storyList = Story.objects.filter(category=cat, tags__in=tags).order_by('menu_order')
            else:
                storyList = Story.objects.filter(category=cat).order_by('menu_order')
                
        elif form.cleaned_data['category_archive']:
            cat = Category.objects.get(slug='archive')
            if tags:
                storyList = Story.objects.filter(category=cat, tags__in=tags).order_by('menu_order')
            else:
                storyList = Story.objects.filter(category=cat).order_by('menu_order')
                
        filtered_list['story_list'] = getFilteredCategory(search, language_code, storyList)
        background_vid = {}
        try:
            cat = Category.objects.get(slug='category-sea');
            background_vid = Background_Video.objects.get(category=cat)
        except Background_Video.DoesNotExist:  
            pass
        
        return render_to_response('story_database/search.html', {'form':form, "filtered_list":filtered_list,"background_video":background_vid, "language":language_code}, context_instance=RequestContext(request))
    else:    
      return render_to_response('story_database/search.html', {'form':form, "language":language_code}, context_instance=RequestContext(request))
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
  template_object['site_categories'] = Category.objects.all()
  template_object['stories_in_category'] = getStoriesInCategory(request, story.category, language)
  template_object['category_sea_stories'] = getStoriesInCategory(request, "category-sea", language)
  template_object['category_land_stories'] = getStoriesInCategory(request, "category-land", language)
  template_object['english_link'] = getEnglishLink(request) 
  template_object['spanish_link'] = getSpanishLink(request)
  template_object['resource_list'] = []
  template_object['research_list'] = []
    
  return template_object
  
def getLanguageForArticle(article, language, request):
    template_object = {}
    
    chapters = article.article_chapter.all()
    
    chap_obj = []
    for chapter in chapters:
        chap_translation = chapter.translations.get(language_code=language)
        chap={}
        chap['headline'] = chap_translation.headline
        chap['subheadline'] = chap_translation.subheadline
        chap['body_text'] = chap_translation.body_text
        chap['infographics'] = chap_translation.interactives.all()
        
        videos = []
        translated_videos = chapter.videos.all()
        for vid in translated_videos:
            videos.append(buildVideoObject(vid))
            
        chap['videos'] = videos
        if chapter.pano_head:
            chap['pano_head'] = chapter.pano_head.url
            
        chap_obj.append(chap)
    template_object["chapters"] = chap_obj
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
        video_obj['poster_frame'] = video.poster_frame.url
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
            
        

def getResearchList(category, language):
  retVal = []
  researchList = Research.objects.filter(category=category)

  try:
    for research in researchList:
      researchTrans = Research_Translation.objects.get(parent=research, language_code=language)
      retVal.append(researchTrans)
  except Research_Translation.DoesNotExist:
    retVal = []

  return retVal

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
  

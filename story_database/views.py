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

def featured_story_page(request, story_slug, language_code='en'):
  return render_to_response(
            'story_database/featured.html',
            getLanguageForStory( getStoryBySlug(request, story_slug), language_code, request, False ),
            context_instance=RequestContext(request)
        )

def about(request, language_code='en'):
  return render_to_response(
            'story_database/about.html',
            getAboutPage(language_code, request),
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


def credits(request, language_code='en'):
  return render_to_response('story_database/credits.html', {'foo':'bar', 'language':language_code})

def testing(request):
  pp = PrettyPrinter()
  return render_to_response('story_database/testTemplate.html', {'output': pp.pformat( getLanguageForStory( getStoryByPK(1), 'en', request ) ) }, context_instance=RequestContext(request));




#utility functions
def getAboutPage(language, request):
    about_page_content = {}
    about_page_content['language'] = language
    
    try:
        about_page = About_Page.objects.get(pk=1)
        about_page_translation = About_Page_Translation.objects.get(parent=about_page, language_code=language)
        relatedContent = Related_Content_Translation.objects.get(parent=about_page_translation.related_content, language_code=language)
        
        about_page_content['research_list'] = []
        about_page_content['story'] = about_page_translation
        about_page_content['resource_list'] = Resources.objects.all()
        about_page_content['related_content_list'] = retrieveRelatedContent(relatedContent, language)
        about_page_content['english_link'] = getEnglishLink(request)
        about_page_content['spanish_link'] = getSpanishLink(request)
        about_page_content['category_sea_stories'] = getStoriesInCategory(request, "category-sea", language)
        about_page_content['category_land_stories'] = getStoriesInCategory(request, "category-land", language)
        about_page_content['background_video'] = {}
        about_page_content['is_mobile'] = request.is_mobile
        try:
          about_page_content['background_video'] = Background_Video.objects.get(id=7)
        except Background_Video.DoesNotExist:
          pass
        
        about_page_content['title_card'] = getAboutPageTitleCard(language)
        
        return about_page_content
    except About_Page.DoesNotExist:
        return Http404;
    except About_Page_Translation.DoesNotExist:
        raise Http404
    except Related_Content_Translation.DoesNotExist:
        about_page_content["related_content"] = {}
        return about_page_content

def getAboutPageTitleCard(language):
  try:
    titleCard = Title_Card.objects.get(slug='about-page-title')
    titleCardTrans = Title_Card_Translation.objects.get(parent=titleCard, language_code=language)
    return titleCardTrans.title_card
  except Title_Card.DoesNotExist:
    return {}

def getFeaturedStoryPage():
  
  try:
      featured_story_collection = FeaturedStory.objects.get(name="Main Page")
      return featured_story_collection.featuredstoryitem_set.all()[0].page
  except FeaturedStory.DoesNotExist:
      raise Http404
  

def getStoryByPK(primaryKey):
  try:
    story = Story.objects.get(pk=primaryKey)
  except Story.DoesNotExist:
    print "Story doesn't exist, getStoryByPK"
    raise Http404
  
  return story

def getStoryBySlug(request, storySlug):
  try:
      
    if request.session.get('isECUADOR') == True and storySlug == 'forbidden-refuge':
        raise Http404  

    story = StoryPage.objects.get(slug=storySlug)
    
  except StoryPage.DoesNotExist:
    raise Http404

  return story

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

def getStoriesByCategory(request, cat, language):
  retVal = []
  
  try:
    storiesInCategory = Story.objects.filter(category=cat).order_by('menu_order')
  except Story.DoesNotExist:
      
    pass
  
  try:
    for story in storiesInCategory:
      if request.session.get('isECUADOR') == False:  
        
          storyObject = {}
          storyTrans = Story_Translation.objects.get(parent=story, language_code=language)

          if storyTrans.featured_video != None:
              storyObject["slug"] = story.slug
              storyObject["thumbnail"] = storyTrans.featured_video.thumbnail
              storyObject["title"] = storyTrans.featured_video.title

          retVal.append(storyObject)
          
      elif request.session.get('isECUADOR') == True and story.slug != 'forbidden-refuge':
          storyObject = {}
          storyTrans = Story_Translation.objects.get(parent=story, language_code=language)

          if storyTrans.featured_video != None:
              storyObject["slug"] = story.slug
              storyObject["thumbnail"] = storyTrans.featured_video.thumbnail
              storyObject["title"] = storyTrans.featured_video.title

          retVal.append(storyObject)
          
  except Story_Translation.DoesNotExist:
    pass
  
  return retVal

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

def retrieveRelatedContent(relatedContent, language):
  related_content_list = [];
  photoGalleries = relatedContent.photo_galleries.all()
  infographics = relatedContent.infographics.all()
  videos = relatedContent.videos.all()
  
  try:
    for photoGallery in photoGalleries:
      photoGalleryTrans = Photo_Gallery_Translation.objects.get(parent=photoGallery, language_code=language)
      content = {}
      content['headline'] = photoGalleryTrans.title
      content['thumbnail'] = photoGallery.thumbnail
      content['description'] = photoGalleryTrans.description
      content['link'] = 'http://www.google.com'
      content['type'] = 'photo_gallery' 
      #Add photo galleries content
      related_content_list.append(content)

  except Photo_Gallery_Translation.DoesNotExist:
    pass
  
  try:
    for infographic in infographics:
      infographicTrans = Infographic_Translation.objects.get(parent=infographic, language_code=language)
      content = {}
      content['headline'] = infographicTrans.title
      content['thumbnail'] = infographicTrans.thumbnail
      content['description'] = infographicTrans.description
      content['link'] = infographicTrans.infographic_files.url
      content['type'] = 'infographic'
      #Add infographics related content to list
      related_content_list.append(content)

  except Infographic_Translation.DoesNotExist:
    pass

  
  for video in videos:
    content = {}
    content['headline'] = video.title
    content['description'] = video.description
    content['thumbnail'] = video.thumbnail
    content['vimeo_id'] = video.vimeo_id
    content['type'] = 'video'
    #Add video related content to list
    related_content_list.append(content)
 
  return related_content_list

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
  

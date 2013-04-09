from story_database.models import *
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response
from story_api.serializers import *
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer, JSONPRenderer

@api_view(['GET'])
def api_root(request, format=None):
    """
    The entry endpoint of our API.
    """
    return Response({
        'stories': reverse('story-list', request=request),
    })

class NavView(APIView):
    renderer_classes = (JSONRenderer, JSONPRenderer)
    
    def get(self, request, format=None):
        if 'language' in request.QUERY_PARAMS:
            lang = request.QUERY_PARAMS['language']
        else:
            lang = 'en'
        response = {}
        catList = []
        try:
            for menu in Menu.objects.all():
                catList.append(MenuSerializer())
                
        except CategoryTranslation.DoesNotExist:
            pass   
        response['navigation'] = catList
        
        serializer = MenuSerializer(instance=Menu.objects.all(), many=True)
        data = serializer.data 
        return Response(data)

class StoryList(generics.ListAPIView):
    """
    API endpoint that represents a list of Stories.
    """
    model = StoryPage
    serializer_class = StorySerializer
    
class StoryDetail(generics.RetrieveAPIView):
    """
    API endpoint that represents a single Story.
    """
    model = StoryPage
    serializer_class = StorySerializer    

class StoryTranslationList(generics.ListAPIView):
    """
    API endpoint that represents a list of StoryTranlastions.
    """
    model = StoryPageTranslation
    serializer_class = StoryTranslationSerializer
    
class StoryTranslationDetail(generics.RetrieveAPIView):
    """
    API endpoint that represents a list of StoryTranlastions.
    """
    model = StoryPageTranslation
    serializer_class = StoryTranslationSerializer


    
class VideoDetail(generics.RetrieveAPIView):
    """
    API endpoint for video
    """
    model = Video
    serializer_class = VideoSerializer
    
class CategoryDetail(generics.RetrieveAPIView):
    model = Category
    serializer_class = CategorySerializer
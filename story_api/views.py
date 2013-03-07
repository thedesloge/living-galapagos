from story_database.models import *
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response
from story_api.serializers import StorySerializer

@api_view(['GET'])
def api_root(request, format=None):
    """
    The entry endpoint of our API.
    """
    return Response({
        'stories': reverse('story-list', request=request),
    })

class StoryList(generics.ListCreateAPIView):
    """
    API endpoint that represents a list of users.
    """
    model = StoryPage
    serializer_class = StorySerializer

class StoryDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that represents a single user.
    """
    model = StoryPage
    serializer_class = StorySerializer
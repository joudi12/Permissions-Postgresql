from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView,RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView

from .serializer import SongSerializer
from .models import Song
from .permissions import PermissionsClass

# Create your views here.
class SongsListView(ListAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = (PermissionsClass,)

class SongDetailsView(RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = (PermissionsClass,)



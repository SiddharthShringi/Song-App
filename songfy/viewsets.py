from rest_framework import viewsets
from rest_framework.response import Response
from songfy.models import Song, Artist, Genre, Playlist
from songfy.serializers import SongSerializer


class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

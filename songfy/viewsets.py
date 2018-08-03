from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from songfy.models import Song, Artist, Genre, Playlist
from songfy.serializers import SongSerializer, ArtistSerializer, GenreSerializer, PlaylistSerializer
from rest_framework.permissions import IsAuthenticated


class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True)
    def songs(self, request, *args, **kwargs):
        artist = self.get_object()
        songs = artist.songs.all()
        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data)


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True)
    def songs(self, *args, **kwargs):
        genre = self.get_object()
        songs = genre.songs.all()
        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data)


class PlaylistViewSet(viewsets.ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

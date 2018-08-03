from rest_framework import serializers
from songfy.models import Song, Artist, Playlist, Genre


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('title', 'duration', 'genre', 'artist', 'user')


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('name', 'user')


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('name', 'user')


class PlaylistSerializer(serializers.ModelSerializer):
    song = serializers.StringRelatedField(many=True)

    class Meta:
        model = Playlist
        fields = ('name', 'song', 'user')

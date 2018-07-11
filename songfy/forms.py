from django import forms
from .models import Song, Artist, Genre, Playlist


class SongForm(forms.ModelForm):

    class Meta:
        model = Song
        fields = ('title', 'duration', 'genre', 'artist')


class ArtistForm(forms.ModelForm):

    class Meta:
        model = Artist
        fields = ('name', )


class GenreForm(forms.ModelForm):

    class Meta:
        model = Genre
        fields = ('name', )


class PlaylistForm(forms.ModelForm):

    class Meta:
        model = Playlist
        fields = ('name', 'song')

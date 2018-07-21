from django import forms
from .models import Song, Artist, Genre, Playlist


class SongForm(forms.ModelForm):

    class Meta:
        model = Song
        fields = ('title', 'duration', 'genre', 'artist')

    def __init__(self, user, *args, **kwargs):
        super(SongForm, self).__init__(*args, **kwargs)
        self.fields['genre'].queryset = Genre.objects.filter(user=user)
        self.fields['artist'].queryset = Artist.objects.filter(user=user)


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
        widgets = {'song': forms.CheckboxSelectMultiple}

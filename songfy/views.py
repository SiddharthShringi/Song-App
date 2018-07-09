from django.shortcuts import render, get_object_or_404
from .models import Song, Artist, Genre, Playlist


def home(request):
    songs = Song.objects.all().order_by('title')
    return render(request, 'songfy/home.html', {'songs': songs})


def artist_lst(request):
    artists = Artist.objects.all().order_by('name')
    return render(request, 'songfy/artist.html', {'artists': artists})


def genre_lst(request):
    genres = Genre.objects.all().order_by('name')
    return render(request, 'songfy/genre.html', {'genres': genres})


def playlist_lst(request):
    playlists = Playlist.objects.all().order_by('name')
    return render(request, 'songfy/playlist.html', {'playlists': playlists})


def artist_song(request, pk):
    artist = get_object_or_404(Artist, pk=pk)
    artists = Artist.objects.all().order_by('name')
    songs = artist.songs.all()
    return render(request, 'songfy/artist_song.html', {'songs': songs, 'artists': artists})


def genre_song(request, pk):
    genre = get_object_or_404(Genre, pk=pk)
    genres = Genre.objects.all().order_by('name')
    songs = genre.songs.all()
    return render(request, 'songfy/genre_song.html', {'songs': songs, 'genres': genres})


def playlist_song(request, pk):
    playlist = get_object_or_404(Playlist, pk=pk)
    playlists = Playlist.objects.all().order_by('name')
    songs = playlist.song.all()
    return render(request, 'songfy/playlist_song.html', {'songs': songs, 'playlists': playlists})

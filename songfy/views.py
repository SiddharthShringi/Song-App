from django.shortcuts import render, get_object_or_404, redirect
from .models import Song, Artist, Genre, Playlist
from .forms import SongForm, ArtistForm, GenreForm, PlaylistForm


def home(request):
    songs = Song.objects.all().order_by('title')
    return render(request, 'songfy/home.html', {'songs': songs})


def song_detail(request, pk):
    song = get_object_or_404(Song, pk=pk)
    return render(request, 'songfy/song_detail.html', {'song': song})


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
    artist_obj = get_object_or_404(Artist, pk=pk)
    artists = Artist.objects.all().order_by('name')
    return render(request, 'songfy/artist_song.html', {'artist_obj': artist_obj, 'artists': artists})


def genre_song(request, pk):
    genre_obj = get_object_or_404(Genre, pk=pk)
    genres = Genre.objects.all().order_by('name')
    return render(request, 'songfy/genre_song.html', {'genre_obj': genre_obj, 'genres': genres})


def playlist_song(request, pk):
    playlist_obj = get_object_or_404(Playlist, pk=pk)
    playlists = Playlist.objects.all().order_by('name')
    return render(request, 'songfy/playlist_song.html', {'playlist_obj': playlist_obj, 'playlists': playlists})


def add_song(request):
    if request.method == 'POST':
        form = SongForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        form = SongForm()
    return render(request, 'songfy/add_edit_song.html', {'form': form})


def edit_song(request, pk):
    song = get_object_or_404(Song, pk=pk)
    if request.method == 'POST':
        form = SongForm(request.POST, instance=song)
        if form.is_valid():
            form.save()
            return redirect('/song/' + str(song.pk))
    else:
        form = SongForm(instance=song)
    return render(request, 'songfy/add_edit_song.html', {'form': form})


def add_artist(request):
    if request.method == "POST":
        form = ArtistForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/artists')
    else:
        form = ArtistForm()
    return render(request, 'songfy/add_artist.html', {'form': form})


def add_genre(request):
    if request.method == "POST":
        form = GenreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/genres')
    else:
        form = GenreForm()
    return render(request, 'songfy/add_genre.html', {'form': form})


def add_playlist(request):
    if request.method == "POST":
        form = PlaylistForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/playlists')
    else:
        form = PlaylistForm()
    return render(request, 'songfy/add_playlist.html', {'form': form})


def song_delete(request, pk):
    song = get_object_or_404(Song, pk=pk)
    song.delete()
    return redirect('/')


def artist_delete(request, pk):
    artist = get_object_or_404(Artist, pk=pk)
    artist.delete()
    return redirect('/artists')


def genre_delete(request, pk):
    genre = get_object_or_404(Genre, pk=pk)
    genre.delete()
    return redirect('/genres')


def playlist_delete(request, pk):
    playlist = get_object_or_404(Playlist, pk=pk)
    playlist.delete()
    return redirect('/playlists')

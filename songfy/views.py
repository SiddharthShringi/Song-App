from django.shortcuts import render, get_object_or_404, redirect
from .models import Song, Artist, Genre, Playlist
from .forms import SongForm, ArtistForm, GenreForm, PlaylistForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate


@login_required
def home(request):
    if request.user.is_authenticated:
        songs = Song.objects.all().filter(user=request.user).order_by('title')
        return render(request, 'songfy/home.html', {'songs': songs})


def song_detail(request, pk):
    song = get_object_or_404(Song, pk=pk)
    return render(request, 'songfy/song_detail.html', {'song': song})


@login_required
def artist_lst(request):
    if request.user.is_authenticated:
        artists = Artist.objects.all().filter(user=request.user).order_by('name')
        return render(request, 'songfy/artist.html', {'artists': artists})


@login_required
def genre_lst(request):
    if request.user.is_authenticated:
        genres = Genre.objects.all().filter(user=request.user).order_by('name')
        return render(request, 'songfy/genre.html', {'genres': genres})


@login_required
def playlist_lst(request):
    if request.user.is_authenticated:
        playlists = Playlist.objects.all().filter(user=request.user).order_by('name')
        return render(request, 'songfy/playlist.html', {'playlists': playlists})


def artist_song(request, pk):
    if request.user.is_authenticated:
        artist_obj = get_object_or_404(Artist, pk=pk)
        artists = Artist.objects.all().filter(user=request.user).order_by('name')
        return render(request, 'songfy/artist_song.html', {'artist_obj': artist_obj, 'artists': artists})


def genre_song(request, pk):
    if request.user.is_authenticated:
        genre_obj = get_object_or_404(Genre, pk=pk)
        genres = Genre.objects.all().filter(user=request.user).order_by('name')
        return render(request, 'songfy/genre_song.html', {'genre_obj': genre_obj, 'genres': genres})


def playlist_song(request, pk):
    if request.user.is_authenticated:
        playlist_obj = get_object_or_404(Playlist, pk=pk)
        playlists = Playlist.objects.all().filter(user=request.user).order_by('name')
        return render(request, 'songfy/playlist_song.html', {'playlist_obj': playlist_obj, 'playlists': playlists})


@login_required
def add_song(request):
    if request.method == 'POST':
        form = SongForm(request.POST)
        if form.is_valid():
            song = form.save(commit=False)
            song.user = request.user
            song.save()
            return redirect('/')

    else:
        form = SongForm()
    return render(request, 'songfy/add_edit_song.html', {'form': form})


@login_required
def edit_song(request, pk):
    song = get_object_or_404(Song, pk=pk)
    if request.method == 'POST':
        form = SongForm(request.POST, instance=song)
        if form.is_valid():
            form.save()
            return redirect('songfy:song_detail', pk=song.id)
    else:
        form = SongForm(instance=song)
    return render(request, 'songfy/add_edit_song.html', {'form': form})


@login_required
def add_artist(request):
    if request.method == "POST":
        form = ArtistForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/artists')
    else:
        form = ArtistForm()
    return render(request, 'songfy/add_artist.html', {'form': form})


@login_required
def add_genre(request):
    if request.method == "POST":
        form = GenreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/genres')
    else:
        form = GenreForm()
    return render(request, 'songfy/add_genre.html', {'form': form})


@login_required
def add_playlist(request):
    if request.method == "POST":
        form = PlaylistForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/playlists')
    else:
        form = PlaylistForm()
    return render(request, 'songfy/add_playlist.html', {'form': form})


@login_required
def edit_playlist(request, pk):
    playlist = get_object_or_404(Playlist, pk=pk)
    if request.method == "POST":
        form = PlaylistForm(request.POST, instance=playlist)
        if form.is_valid():
            form.save()
            return redirect('songfy:playlist_song', pk=playlist.id)
    else:
        form = PlaylistForm(instance=playlist)
    return render(request, 'songfy/add_playlist.html', {'form': form})


@login_required
def song_delete(request, pk):
    song = get_object_or_404(Song, pk=pk)
    song.delete()
    return redirect('/')


@login_required
def artist_delete(request, pk):
    artist = get_object_or_404(Artist, pk=pk)
    artist.delete()
    return redirect('/artists')


@login_required
def genre_delete(request, pk):
    genre = get_object_or_404(Genre, pk=pk)
    genre.delete()
    return redirect('/genres')


@login_required
def playlist_delete(request, pk):
    playlist = get_object_or_404(Playlist, pk=pk)
    playlist.delete()
    return redirect('/playlists')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'songfy/signup.html', {'form': form})

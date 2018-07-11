from django.urls import path
from . import views

app_name = 'songfy'

urlpatterns = [
    path('', views.home, name='home'),
    path('song/<int:pk>', views.song_detail, name='song_detail'),
    path('artists', views.artist_lst, name='artist_lst'),
    path('genres', views.genre_lst, name='genre_lst'),
    path('playlists', views.playlist_lst, name='playlist_lst'),
    path('artists/artist/<int:pk>', views.artist_song, name='artist_song'),
    path('genres/genre/<int:pk>', views.genre_song, name='genre_song'),
    path('playlists/playlist/<int:pk>', views.playlist_song, name='playlist_song'),
    path('song/new', views.add_song, name='add_song'),
    path('song/edit/<int:pk>', views.edit_song, name='edit_song'),
    path('artist/new', views.add_artist, name="add_artist"),
    path('genre/new', views.add_genre, name='add_genre'),
    path('playlist/new', views.add_playlist, name='add_playlist'),
]

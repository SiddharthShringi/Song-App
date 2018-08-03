from django.urls import path
from django.conf.urls import include
from . import views
from rest_framework.routers import DefaultRouter
from . import viewsets

app_name = 'songfy'

router = DefaultRouter()
router.register('songs', viewsets.SongViewSet)
router.register('artists', viewsets.ArtistViewSet)
router.register('genres', viewsets.GenreViewSet)
router.register('playlists', viewsets.PlaylistViewSet)

urlpatterns = [
    path('', views.home, name='home'),
    path('song/<int:pk>', views.song_detail, name='song_detail'),
    path('artists', views.artist_lst, name='artist_lst'),
    path('genres', views.genre_lst, name='genre_lst'),
    path('playlists', views.playlist_lst, name='playlist_lst'),
    path('artists/<int:pk>', views.artist_song, name='artist_song'),
    path('genres/<int:pk>', views.genre_song, name='genre_song'),
    path('playlists/<int:pk>', views.playlist_song, name='playlist_song'),
    path('song/new', views.add_song, name='add_song'),
    path('song/edit/<int:pk>', views.edit_song, name='edit_song'),
    path('artist/new', views.add_artist, name='add_artist'),
    path('genre/new', views.add_genre, name='add_genre'),
    path('playlist/new', views.add_playlist, name='add_playlist'),
    path('playlist/<int:pk>/edit', views.edit_playlist, name='edit_playlist'),
    path('song/<int:pk>/delete', views.song_delete, name='song_delete'),
    path('artist/<int:pk>/delete', views.artist_delete, name='artist_delete'),
    path('genre/<int:pk>/delete', views.genre_delete, name='genre_delete'),
    path('playlist/<int:pk>/delete', views.playlist_delete, name='playlist_delete'),
    path('signup', views.signup, name='signup'),
    path('api/', include(router.urls))
]

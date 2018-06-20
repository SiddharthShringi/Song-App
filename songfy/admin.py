from django.contrib import admin
from .models import Song, Genre, Artist, Playlist
# Register your models here.
admin.site.register(Song)
admin.site.register(Artist)
admin.site.register(Genre)
admin.site.register(Playlist)

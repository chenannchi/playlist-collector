from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('playlists/', views.playlists_index, name='playlists_index'),
  path('playlists/<int:playlist_id>/', views.playlists_detail, name='playlists_detail'),
  path('playlists/create/', views.PlaylistCreate.as_view(), name='Playlists_create'),
  path('playlists/<int:pk>/update/', views.playlistUpdate.as_view(), name='playlists_update'),
  path('playlists/<int:pk>/delete/', views.playlistDelete.as_view(), name='playlists_delete'),
  path('playlists/<int:playlist_id>/add_review/', views.add_review, name='add_review'),
  path('songs/create/', views.SongCreate.as_view(), name='songs_create'),
  path('songs/<int:pk>/', views.SongDetail.as_view(), name='songs_detail'),
  path('songs/', views.SongList.as_view(), name='songs_index'),
]
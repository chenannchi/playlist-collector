from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('playlists/', views.playlists_index, name='playlists_index'),
  path('playlists/<int:playlist_id>/', views.playlists_detail, name='playlists_detail'),
  path('playlists/create/', views.PlaylistCreate.as_view(), name='Playlists_create'),
]
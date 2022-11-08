from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Playlist
# Create your views here.

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def playlists_index(request):
  playlists = Playlist.objects.all()
  return render(request, 'playlists/index.html',{'playlists':playlists})

def playlists_detail(request, playlist_id):
  playlist = Playlist.objects.get(id=playlist_id)
  return render(request, 'playlists/detail.html', { 'playlist': playlist })

class PlaylistCreate(CreateView):
  model = Playlist
  fields = '__all__'

class playlistUpdate(UpdateView):
  model = Playlist
  # Let's disallow the renaming of a playlist by excluding the name field!
  fields = ['description']

class playlistDelete(DeleteView):
  model = Playlist
  success_url = '/playlists/'
from django.shortcuts import render
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
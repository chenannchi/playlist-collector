from django.shortcuts import render

# Create your views here.

# Add the following import
from django.http import HttpResponse


class Playlist:
  def __init__(self, name, description):
    self.name = name
    self.description = description
  
playlists = [
  Playlist('Sleep','Gentle ambient piano to help you fall asleep.'),
  Playlist('Lofi Work', 'Ideal for working from home or at the office, curated to keep you focused!'),
  Playlist('Morning K-Pop', 'Everyday shoud be a happy day when you listen to this fun K-Pop playlist.'),
  Playlist('Evening Acoustic', 'Keep your night easy and light with this acoustic mix.'),
  Playlist('The Rose', 'Welcome to healing paradise! Let\'s heal together!'),
]

# Define the home view
def home(request):
  return HttpResponse('<h1>home page</h1>')

def about(request):
  return render(request, 'about.html')

def playlists_index(request):
  return render(request, 'playlists/index.html',{'playlists':playlists})
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Playlist, Song
from .forms import ReviewForm
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
  review_form = ReviewForm()
  return render(request, 'playlists/detail.html', { 'playlist': playlist, "review_form":review_form })

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

def add_review(request, playlist_id):
  # create a ModelForm instance using the data in request.POST
  form = ReviewForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_review = form.save(commit=False)
    new_review.playlist_id = playlist_id
    new_review.save()
  return redirect('playlists_detail', playlist_id=playlist_id)

class SongCreate(CreateView):
  model = Song
  fields = '__all__'

class SongList(ListView):
  model = Song

class SongDetail(DetailView):
  model = Song
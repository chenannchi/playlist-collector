from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from .models import Playlist, Song
from .forms import ReviewForm
# Create your views here.

# Define the home view
class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

def playlists_index(request):
  playlists = Playlist.objects.all()
  return render(request, 'playlists/index.html',{'playlists':playlists})

def playlists_detail(request, playlist_id):
  playlist = Playlist.objects.get(id=playlist_id)
  songs_playlist_doesnt_include = Song.objects.exclude(id__in = playlist.songs.all().values_list('id'))
  review_form = ReviewForm()
  return render(request, 'playlists/detail.html', { 'playlist': playlist, "review_form":review_form,"songs":songs_playlist_doesnt_include })

class PlaylistCreate(CreateView):
  model = Playlist
  fields = ["name", "description"]

  def form_valid(self, form):
    # Assign the logged in user (self.request.user)
    form.instance.user = self.request.user
    # Let the CreateView do its job as usual
    return super().form_valid(form)

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

class SongUpdate(UpdateView):
  model = Song
  fields = ["title", "singer", "composer", "album"]

class SongDelete(DeleteView):
  model = Song
  success_url = '/songs/'

def assoc_song(request, playlist_id, song_id):
  # Note that you can pass a toy's id instead of the whole object
  Playlist.objects.get(id=playlist_id).songs.add(song_id)
  return redirect('playlists_detail', playlist_id=playlist_id)
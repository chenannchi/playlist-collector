from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Playlist, Song
from .forms import ReviewForm
# Create your views here.

# Define the home view
class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

@login_required
def playlists_index(request):
  playlists = Playlist.objects.filter(user=request.user)
  return render(request, 'playlists/index.html',{'playlists':playlists})

@login_required
def playlists_detail(request, playlist_id):
  playlist = Playlist.objects.get(id=playlist_id)
  songs_playlist_doesnt_include = Song.objects.exclude(id__in = playlist.songs.all().values_list('id'))
  review_form = ReviewForm()
  return render(request, 'playlists/detail.html', { 'playlist': playlist, "review_form":review_form,"songs":songs_playlist_doesnt_include })

class PlaylistCreate(LoginRequiredMixin, CreateView):
  model = Playlist
  fields = ["name", "description"]

  def form_valid(self, form):
    # Assign the logged in user (self.request.user)
    form.instance.user = self.request.user
    # Let the CreateView do its job as usual
    return super().form_valid(form)

class playlistUpdate(LoginRequiredMixin, UpdateView):
  model = Playlist
  # Let's disallow the renaming of a playlist by excluding the name field!
  fields = ['description']

class playlistDelete(LoginRequiredMixin, DeleteView):
  model = Playlist
  success_url = '/playlists/'

@login_required
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

class SongCreate(LoginRequiredMixin, CreateView):
  model = Song
  fields = '__all__'

class SongList(LoginRequiredMixin, ListView):
  model = Song

class SongDetail(LoginRequiredMixin, DetailView):
  model = Song

class SongUpdate(LoginRequiredMixin, UpdateView):
  model = Song
  fields = ["title", "singer", "composer", "album"]

class SongDelete(LoginRequiredMixin, DeleteView):
  model = Song
  success_url = '/songs/'

@login_required
def assoc_song(request, playlist_id, song_id):
  # Note that you can pass a toy's id instead of the whole object
  Playlist.objects.get(id=playlist_id).songs.add(song_id)
  return redirect('playlists_detail', playlist_id=playlist_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in
      login(request, user)
      return redirect('playlists_index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)
  # Same as: return render(request, 'signup.html', {'form': form, 'error_message': error_message})
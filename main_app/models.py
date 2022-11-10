from django.db import models
from django.urls import reverse
# Create your models here.

RATINGS=(
  (5, 5),(4, 4),(3,3),(2, 2),(1, 1)
)

class Song(models.Model):
  title = models.CharField(max_length=100)
  singer = models.CharField(max_length=50)
  composer = models.CharField(max_length=50, default="-")
  album = models.CharField(max_length=50, default="-")

  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return reverse('songs_detail', kwargs={'pk': self.id})

class Playlist(models.Model):
  name = models.CharField(max_length=100)
  description = models.CharField(max_length=100)
  songs = models.ManyToManyField(Song)


  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('playlists_detail', kwargs={'playlist_id': self.id})

  def average_rating(self):
    if len(self.review_set.all()) > 0:
      total = 0
      for review in self.review_set.all():
        total+=review.rating
      return f"{total / len(self.review_set.all()):.1f}⭐"
    else:
      return ""

# Add new Feeding model below Cat model
class Review(models.Model):
  date = models.DateField(auto_now_add=True)
  author = models.CharField(max_length=20)
  comment = models.TextField(max_length=100)
  rating = models.IntegerField(choices=RATINGS, default=5)
  playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
  
  def __str__(self):
    return f"{self.author} left a comment({self.comment} on {self.date})."

  class Meta:
    ordering = ['-date']


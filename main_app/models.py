from django.db import models
from django.urls import reverse
# Create your models here.

class Playlist(models.Model):
  name = models.CharField(max_length=100)
  description = models.CharField(max_length=100)

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('playlists_detail', kwargs={'playlist_id': self.id})

# Add new Feeding model below Cat model
class Review(models.Model):
  date = models.DateField(auto_now_add=True)
  author = models.CharField(max_length=20)
  comment = models.TextField(max_length=100)
  playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
  
  def __str__(self):
    return f"{self.author} left a comment({self.comment} on {self.date})."

  
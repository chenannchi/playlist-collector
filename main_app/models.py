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


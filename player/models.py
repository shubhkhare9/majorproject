from django.db import models

# Create your models here.

class Playlist(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Artist(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Song(models.Model):
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='songs')    
    audio_file = models.FileField(upload_to='songs/')
    cover_image = models.ImageField(upload_to='covers/', blank=True, null=True)
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE, related_name='songs', null=True, blank=True)

    def __str__(self):
        return self.title
    
# class Song(models.Model):
#     title = models.CharField(max_length=100)
#     artist = models.CharField(max_length=100)
#     audio_file = models.FileField(upload_to='songs/')
#     cover_image = models.ImageField(upload_to='covers/', blank=True, null=True)
#     playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE, related_name='songs')

#     def __str__(self):
#         return f"{self.title} ({self.playlist.name})"
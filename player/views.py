from django.shortcuts import render, redirect
from .forms import SongForm
from .models import Song, Playlist, Artist
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout


# Create your views here.
def index(request):
    return render(request, 'player/index.html')

def about(request):
    return render(request, 'player/about.html')

def login_view(request):
    return render(request, 'player/login.html')

def signup_view(request):
    return render(request, 'player/signup.html')

def custom_logout_view(request):
    logout(request)
    return render(request, 'player/logged_out.html')

def song_list(request):
    playlists = Playlist.objects.prefetch_related('songs').all()
    return render(request, 'player/songs.html', {'playlists': playlists})

def upload_song(request):
    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('player:songs')
    else:
        form = SongForm()
    return render(request, 'player/upload_song.html', {'form': form})

def song_list(request):
    songs = Song.objects.all()
    return render(request, 'player/songs.html', {'songs': songs})

from django.shortcuts import get_object_or_404, redirect

def delete_song(request, pk):
    song = get_object_or_404(Song, pk=pk)
    if request.method == 'POST':
        song.delete()
        return redirect('player:songs')
    return render(request, 'player/delete_song.html', {'song': song})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Django's built-in login URL
    else:
        form = UserCreationForm()
    return render(request, 'player/register.html', {'form': form})

def show_songs(request):
    songs = Song.objects.all()
    return render(request, 'player/songs.html', {'songs': songs})

def playlist_view(request):
    playlists = Playlist.objects.prefetch_related('songs').all()
    return render(request, 'player/playlist.html', {'playlists': playlists})

def artist_view(request):
    artists = Artist.objects.prefetch_related('songs').all()
    return render(request, 'player/artist.html', {'artists': artists})
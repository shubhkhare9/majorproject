from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from .views import custom_logout_view
app_name='player'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('login/', auth_views.LoginView.as_view(template_name='player/login.html'), name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('upload/', views.upload_song, name='upload_song'),
    path('songs/', views.song_list, name='songs'),
    path('songs/delete/<int:song_id>/', views.delete_song, name='delete_song'),
    #path('accounts/', include('django.contrib.auth.urls')),  # Login, logout, password management
    path('register/', views.register, name='register'),
    path('logout/', LogoutView.as_view(template_name='player/logged_out.html'), name='logout'),
    path('custom_logout/', custom_logout_view, name='custom_logout'),
    path('songs/<int:pk>/delete/', views.delete_song, name='delete_song'),
    path('playlist/', views.playlist_view, name='playlist'),
    path('artist/', views.artist_view, name='artist'),

    ]

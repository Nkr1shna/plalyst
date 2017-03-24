from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .forms import UserForm,PlaylistForm,SongForm,AddPreferencesForm
from .models import Playlist,Song


def index(request):
    if not request.user.is_authenticated():
        return render(request, 'login.html')
    else:
        playlists = Playlist.objects.filter(user=request.user)
        query = request.GET.get("q")
        if query:
            playlists = playlists.filter(
                Q(Plalyst_title__icontains=query)
            ).distinct()
            return render(request, 'index.html', {
                'playlists': playlists,
            })
        else:
            return render(request, 'index.html', {'playlists': playlists})


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'login.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                playlists = Playlist.objects.filter(user=request.user)
                return render(request, 'index.html', {'playlists': playlists})
        else:
            return render(request, 'login.html', {'error_message': 'Invalid login'})
    return render(request, 'login.html')


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                playlists = Playlist.objects.filter(user=request.user)
                return render(request, 'index.html', {'playlists': playlists})
    context = {
        "form": form,
    }
    return render(request, 'register.html', context)


def create_playlist(request):
    if not request.user.is_authenticated():
        return render(request, 'login.html')
    else:
        form = PlaylistForm(request.POST or None)
        if form.is_valid():
            playlist = form.save(commit=False)
            playlist.user = request.user
            playlist.save()
            return render(request, 'detail.html', {'playlist': playlist})
        context = {
            "form": form,
        }
        return render(request, 'create_playlist.html', context)


def detail(request, playlist_id):
    if not request.user.is_authenticated():
        return render(request, 'login.html')
    else:
        user = request.user
        playlist = get_object_or_404(Playlist, pk=playlist_id)
        return render(request, 'detail.html', {'playlist': playlist, 'user': user})


def create_song(request, playlist_id):
    form = SongForm(request.POST or None)
    playlist = get_object_or_404(Playlist, pk=playlist_id)
    if form.is_valid():
        playlists_songs = playlist.song_set.all()
        for s in playlists_songs:
            if s.song_title == form.cleaned_data.get("song_title"):
                context = {
                    'playlist': playlist,
                    'form': form,
                    'error_message': 'You already added that song',
                }
                return render(request, 'create_song.html', context)
        song = form.save(commit=False)
        song.playlist = playlist
        song.save()
        songs_count = playlists_songs.count()
        if (songs_count < 7):
            context = {
                'playlist': playlist,
                'form': form,
                'error_message': 'Add minimum of 8 songs',
            }
            return render(request, 'create_song.html', context)
        return render(request, 'detail.html', {'playlist': playlist})
    context = {
        'playlist': playlist,
        'form': form,
    }
    return render(request, 'create_song.html', context)


def delete_playlist(request, playlist_id):
    playlist = Playlist.objects.get(pk=playlist_id)
    playlist.delete()
    playlists = Playlist.objects.filter(user=request.user)
    return render(request, 'index.html', {'playlists': playlists})


def delete_song(request, playlist_id, song_id):
    playlist = get_object_or_404(Playlist, pk=playlist_id)
    song = Song.objects.get(pk=song_id)
    song.delete()
    return render(request, 'detail.html', {'playlist': playlist})


def add_preferences(request,playlist_id):
    form= AddPreferencesForm(request.POST or None)
    playlist = get_object_or_404(Playlist, pk=playlist_id)
    if form.is_valid():
        playlists_preferences = playlist.addpreferences_set.all()
        if form.is_valid():
            preferences = form.save(commit=False)
            preferences.playlist = playlist
            preferences.save()
            return render(request, 'detail.html', {'playlist': playlist})
    context = {
        'playlist': playlist,
        'form': form,
    }
    return render(request, 'add_preferences.html', context)


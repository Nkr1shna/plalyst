from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .forms import UserForm,AlbumForm
from .models import Album


def index(request):
    if not request.user.is_authenticated():
        return render(request, 'login.html')
    else:
        albums = Album.objects.filter(user=request.user)
        query = request.GET.get("q")
        if query:
            albums = albums.filter(
                Q(Plalyst_title__icontains=query)
            ).distinct()
            return render(request, 'index.html', {
                'albums': albums,
            })
        else:
            return render(request, 'index.html', {'albums': albums})


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
                albums = Album.objects.filter(user=request.user)
                return render(request, 'index.html', {'albums': albums})
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
                albums = Album.objects.filter(user=request.user)
                return render(request, 'index.html', {'albums': albums})
    context = {
        "form": form,
    }
    return render(request, 'register.html', context)

def create_album(request):
    if not request.user.is_authenticated():
        return render(request, 'login.html')
    else:
        form = AlbumForm(request.POST or None)
        if form.is_valid():
            album = form.save(commit=False)
            album.user = request.user
            album.save()
            return render(request, 'detail.html', {'album': album})
        context = {
            "form": form,
        }
        return render(request, 'create_album.html', context)


def detail(request, album_id):
    if not request.user.is_authenticated():
        return render(request, 'login.html')
    else:
        user = request.user
        album = get_object_or_404(Album, pk=album_id)
        return render(request, 'detail.html', {'album': album, 'user': user})




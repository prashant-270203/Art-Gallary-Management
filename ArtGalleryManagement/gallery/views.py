from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Artist, Artwork, Exhibition
from .forms import ArtistRegistrationForm  # Ensure this import is correct

def home(request):
    return render(request, "gallery/home.html")

def artist_list(request):
    artists = Artist.objects.all()
    return render(request, "gallery/artist_list.html", {"artists": artists})

def artwork_list(request):
    artworks = Artwork.objects.all()
    return render(request, "gallery/artwork_list.html", {"artworks": artworks})

def exhibition_list(request):
    exhibitions = Exhibition.objects.all()
    return render(request, "gallery/exhibition_list.html", {"exhibitions": exhibitions})

def register_artist(request):
    if request.method == 'POST':
        form = ArtistRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to home or another page after registration
    else:
        form = ArtistRegistrationForm()
    return render(request, 'gallery/register_artist.html', {'form': form})
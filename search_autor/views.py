from django.shortcuts import render
from main.models import Artist


def index(request):
    all_artists = Artist.objects.order_by("artist_name")
    return render(request, 'search_autor/index.html', {"all_artists": all_artists})
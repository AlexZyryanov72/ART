from django.shortcuts import render
from main.models import Artist


def search_autor(request):
    search_query = request.GET.get('q','')
    if search_query:
        all_artists = Artist.objects.filter(artist_name__icontains=search_query).order_by("artist_name")
    else:
        all_artists = Artist.objects.order_by("artist_name")
    return render(request, 'search_autor/index.html', {"all_artists": all_artists})
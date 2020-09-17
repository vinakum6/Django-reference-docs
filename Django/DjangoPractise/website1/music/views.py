from django.shortcuts import render,get_object_or_404
from .models import Album,Song

def index(request):
    all_albums = Album.objects.all()
    return render(request,'music/index.html',{'all_albums':all_albums,})
    
def detail(request,album_id):
    album=get_object_or_404(Album,id=album_id)
    return render(request,'music/details.html',{'album':album})
    
def favorite(request,album_id):
    album=get_object_or_404(Album,id=album_id)
    try:
        selected_song = album.song_set.get(pk=request.POST.get('song'))
    except Exception as ex:
        return render(request,'music/favorite.html',{'album':album,'error_message':'Please select a valid '})
    else:    
        selected_song.is_favorite = True
        selected_song.save()
        return render(request,'music/favorite.html',{'album':album})    
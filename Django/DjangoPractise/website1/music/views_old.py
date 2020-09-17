from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from .models import Album

def index(request):
    all_albums = Album.objects.all()
    template =loader.get_template('music/index.html')
    context = {'all_albums':all_albums,}
    #html = ''
    #for album in all_albums:
    #    url = '/music/'+str(album.id)+'/'
    #    html +='<a href="'+url+'">'+album.album_title+'</a><br>'
    #return HttpResponse('<H1 style="text-decoration:underline;">Welcome to my Music Home Page</H1>'+html)
    return HttpResponse(template.render(context,request))
    
#def detail(request,album_id):
#    return HttpResponse('<h2>Details for Album id:'+str(album_id)+'</h2>')
    
    
    
def detail(request,album_id):
    try:
        album =Album.objects.get(id=album_id)
    except Album.DoesNotExist:
        raise Http404('Oops ..Album id - '+ str(album_id) + ' not Found !!!')
    return render(request,'music/details.html',{'album':album})    
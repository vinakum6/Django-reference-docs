from django.http import HttpResponse

def demoview1(request):
    return HttpResponse('<h2>&nbsp&nbsp&nbsp&nbspThis is your demoview''s first view !!</h2>')
    

def demoview2(request):
    return HttpResponse('<h2>&nbsp&nbsp&nbsp&nbspThis is your demoview''s Second view!!</h2>')    

def dfault(request):
    return HttpResponse('<h1><center>Welcome to Multiview Demo</center></h1>')
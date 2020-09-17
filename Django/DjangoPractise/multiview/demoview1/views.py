from django.http import HttpResponse

def demoview1(request):
    return HttpResponse('<h2>&nbsp&nbsp&nbsp&nbspThis is your first view in Demoview1!!</h2>')
    

def demoview2(request):
    return HttpResponse('<h2>&nbsp&nbsp&nbsp&nbspThis is your Second view in Demoview1!!</h2>')    

def dfault(request):
    return HttpResponse('<h1><center>Welcome to Multiproject and multiview Demo!!!</center></h1>')
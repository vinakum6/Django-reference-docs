from django.urls import path
from demoview1.views import demoview1,demoview2,dfault

urlpatterns = [
    path('',dfault,name='dfault'),
    path('demoview11/',demoview1,name='demoview1'),
    path('demoview12/',demoview2,name='demoview2'),
]

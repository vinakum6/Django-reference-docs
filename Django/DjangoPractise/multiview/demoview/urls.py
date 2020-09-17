from django.urls import path
from demoview.views import demoview1,demoview2,dfault

urlpatterns = [
    path('default/',dfault,name='dfault'),
    path('demoview1/',demoview1,name='demoview1'),
    path('demoview2/',demoview2,name='demoview2'),
]

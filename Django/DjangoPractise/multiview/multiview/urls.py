from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('demoview.urls')),
    path('',include('demoview1.urls')),
]

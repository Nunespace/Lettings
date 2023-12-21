from django.contrib import admin
from django.conf.urls import handler404, handler500
from django.urls import path, include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('lettings/', include('lettings.urls')),
    path('profiles/', include('profiles.urls')),
]

handler404 = views.handler404
handler500 = views.handler500

"""
URL configuration for djangoproject1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.homeview),
    path('about/',views.aboutview),
    path('parentreg/',views.parentregview),
    path('classes/',views.classesview),
    path('gallery/',views.galleryview),
    path('latestnews/',views.latestnewsview),
    path('contact/',views.contactview),
    path('class8/',views.class8view),
    path('class9/',views.class9view),
    path('class10/',views.class10view),
    path('photos/',views.photosview),
    path('videos/',views.videosview),
    path('admins/',views.adminsview),
    path('thanks/',views.thanksview),

]

"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from os import name, stat
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<slug:slug>/', views.post, name='post'),
    path('posts/', views.posts, name='posts'),
    path('admin/', admin.site.urls),

    path('create_post/', views.createPost, name='create_post'),
    path('update_post/<slug:slug>/', views.updatePost, name='update_post'),
    path('delete_post/<slug:slug>/', views.deletePost, name='delete_post'),

    path('send_email/', views.sendEmail, name='send_email'),
    path('ckeditor/', include('ckeditor_uploader.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)


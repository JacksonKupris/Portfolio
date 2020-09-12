from django.http import request
from django.shortcuts import render, HttpResponse

from .models import Post

# Create Views here

def home(request):
    return render(request, 'index.html')


def post(request):
    return render(request, 'post.html')

def posts(request):
    posts = Post.objects.all()


    context ={
        'posts':posts
    }

    return render(request, 'posts.html', context)
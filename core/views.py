from django.shortcuts import render
from .models import Post, Tag

def blog(request):
    posts = Post.objects.all()
    tags = Tag.objects.all()
    return render(request, 'blog.html', {'posts': posts, 'tags': tags})

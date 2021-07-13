from django.shortcuts import render
from .models import Blog_entry

def all_blogs(request):
    projects = Blog_entry.objects.order_by('-data')[:5]
    return render(request, 'blog/all_blogs.html', {'projects':projects})

def all_posts(request):
    projects = Blog_entry.objects.order_by('-data')
    return render(request, 'blog/all_posts.html', {'projects':projects})

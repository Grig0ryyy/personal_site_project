from django.shortcuts import render, get_object_or_404
from .models import Blog_entry

def all_blogs(request):
    projects = Blog_entry.objects.order_by('-data')[:5]
    return render(request, 'blog/all_blogs.html', {'projects':projects})

def all_posts(request):
    projects = Blog_entry.objects.order_by('-data')
    return render(request, 'blog/all_posts.html', {'projects':projects})

def detail(request, blog_id):
    blog = get_object_or_404(Blog_entry, pk=blog_id)
    return render(request, 'blog/detail.html',{'blog':blog})

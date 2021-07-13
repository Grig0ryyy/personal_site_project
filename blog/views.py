from django.shortcuts import render
from .models import Blog_entry

def all_blogs(request):
    projects = Blog_entry.objects.all()
    return render(request, 'blog/all_blogs.html', {'projects':projects})

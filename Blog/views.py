from django.shortcuts import render
from .models import *

# Create your views here.

def Home(request):
    allposts=Blogs.objects.all()
    return render(request,'blog/index.html',{
        'posts':allposts,
        'newposts':RecentPosts()
    })

def Blog(request,blog):
    blog=Blogs.objects.filter(slug=blog).first()
    return render(request,'blog/single-standard.html',{
        'post':blog,
        'newposts':RecentPosts()
    })

def RecentPosts():
    posts=Blogs.objects.order_by('-created_at')[:3]
    return posts
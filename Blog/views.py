from django.shortcuts import render
from .models import *

# Create your views here.

def Home(request):
    return render(request,'blog/index.html',{
        'posts':Blogs.objects.all()
    })

def Blog(request,blog):
    blog=Blogs.objects.filter(slug=blog).first()
    return render(request,'blog/single-standard.html',{
        'post':blog
    })
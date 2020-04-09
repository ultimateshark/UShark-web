from django.shortcuts import render
from .models import *

# Create your views here.

def Home(request):
    return render(request,'blog/index.html',{
        'posts':Blogs.objects.all()
    })

def Blog(request):
    return render(request,'blog/single-standard.html',{
        'post':Blogs.objects.first()
    })
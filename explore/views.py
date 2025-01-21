from django.shortcuts import render , get_object_or_404
from .models import *

# Create your views here.

def all_blogs(request):
    blogs = BlogPost.objects.prefetch_related('images').all()
    return render(request , 'blogs.html' , {'blogs' : blogs})

def single_blog(request , id):
    blog = get_object_or_404(BlogPost , pk=id)
    return render(request , 'blog.html' , {'blog' : blog})

def safety_inst(request):
    return render(request , 'basics/safety_inst.html')

from django.shortcuts import render
from .models import Blog

def all_blogs(request):
    blog_obj=Blog.objects.all()
    return render(request, 'blog/all_blogs.html',{'bo':blog_obj})

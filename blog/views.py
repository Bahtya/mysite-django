from django.shortcuts import render
from .models import Blog
from .models import Tag

def index(request):
    tags = Tag.objects.all() 
    blogs = Blog.objects.all()   
    data={
        "blogs":blogs,
        "tags":tags,
        "isActive1":"active"
    }
    return render(request,"index.html",data)

def about(request):
    blogs = Blog.objects.all()
    return render(request,"about.html")

def contact(request):
    blogs = Blog.objects.all()
    return render(request,"contact.html")

def blog_list(request):
    blogs = Blog.objects.all()
    data={
        "blogs":blogs,
        "isActive2":"active"
    }
    return render(request,"blog_list.html",data)

def blog(request,num):
    res = Blog.objects.get(pk=num)
    data={
        "test" : res.caption ,
        "isActive2":"active"
    }
    return render(request,"blog.html",data)

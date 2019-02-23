from django.core.paginator import Paginator
from django.shortcuts import render
from .models import *

def index(request):
    tags = Tag.objects.all() 
    blogs = Blog.objects.all()   
    data={
        "blogs":blogs,
        "tags":tags,
        "isActive1":"active"#导航栏激活状态
    }
    return render(request,"index.html",data)

def about(request):
    blogs = Blog.objects.all()
    data={
        "isActive3":"active"#导航栏激活状态
    }
    return render(request,"about.html",data)

def contact(request):
    blogs = Blog.objects.all()
    data={
        "isActive4":"active"#导航栏激活状态
    }
    return render(request,"contact.html")

def blog_list(request):
    page = request.GET.get('page',1)#get请求传参数，page如果不存在默认返回1
    blogs = Blog.objects.all()
    paginator=Paginator(blogs,10)#实例化分页器，第一个参数为对象，第二个参数为每页的页数
    page_n = paginator.get_page(page) #返回一个某一页分页器对象，此方式如果page不符合规范，会返回1
    page_countor = page_n.number#number取出当前页的页码
    #优化页码溢出，并每次只显示5页功能实现
    if page_countor <= 3 :
        page_list = page_n.paginator.page_range[:5]
    elif page_countor >= page_n.paginator.num_pages-2:
        page_list = [
            page_n.paginator.num_pages-4,
            page_n.paginator.num_pages-3,
            page_n.paginator.num_pages-2,
            page_n.paginator.num_pages-1,
            page_n.paginator.num_pages
        ]
    else:
        page_list = [
                page_countor-2,
                page_countor-1,
                page_countor,
                page_countor+1,
                page_countor+2
        ]   
    data={
        "page_list":page_list,
        "blogs":page_n,
        "isActive2":"active"#导航栏激活状态
    }
    return render(request,"blog_list.html",data)

def blog(request,num):
    blog = Blog.objects.get(pk=num)#按照传回的参数pk值取出对应的blog对象
    data={
        "blog" : blog ,
        "isActive2":"active"
    }
    return render(request,"blog.html",data)

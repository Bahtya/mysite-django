from django.urls import path, re_path
from blog import views

urlpatterns = [
    path('', views.index),
    path('index', views.index),
    path('about', views.about),
    path('contact', views.contact),
    path('blog_list', views.blog_list),
    #re_path('blog_list/(?P<page>[0-9]+)', views.blog_list),
    re_path('blog/(?P<num>[0-9]+)', views.blog),
]

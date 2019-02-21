from django.urls import path
from blog import views

urlpatterns = [
    path('', views.index),
    path('index', views.index),
    path('about', views.about),
    path('contact', views.contact),
    path('blog_list', views.blog_list),
    path('blog/(?P<num>[0-9]+)', views.blog),
]

# mysite
个人博客模板
###配置视图
    frome django.http import HttpResponse  
    def index(request):  
        return HttpResponse ('This is a view')  
或  
 `return render(request,'app/index.html'),{'模板里的变量名':变量})` 
###配置路由urls.py  
 `from django.conf.urls import url,include`   
 `from django.contrib import admin` 

    urlpaterns=[
        url(r'^'admin/',admin.site.urls),  
        url(r'^',incude('myapp.urls'))  
    ]  
在app目录下创建urls.py：  
 `from django.conf.urls import url`   
 `from . import views` 
 `urlpaterns=[  
    url(r'^$',views.index),
    url(r'^\d+/$',views.),
    ]  `   
###模板  templates目录里  
配置cv>vc

模板路径（settings.py）：  
 `TEMPLATES:{'DIR':[os.path.join(BASE_DIR,'templates'  
]`   
###配置static  
settings.py  
最后一行添加：  
    STATICFILES_DIRS=[
        os.path.join(BASE_DIR,'static')
    ]  
上传目录：  
    MDEIA_ROOT=os.path.join(BASE_DIR,r'static/mdeia')
###模板语法  
变量语法：{{变量名}}  
语句语法：{%语句%}

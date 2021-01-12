# mysite

[lw个人博客](http://148.70.69.254/)

开发语言：`Python`

后端应用框架：`Django2.1`

前端框架：`Bootstrap`(css)、`jQuery`(js)

web服务：Apache、Nginx皆可用

参考：

[Django开发手册](https://docs.djangoproject.com/en/2.1/)

[Bootstrap中文网](http://www.bootcss.com/)

[jQuery插件库](http://www.jq22.com/)

### 目录结构

```shell
mysite
├── blog #blog应用层
│   ├── admin.py #配置后台
│   ├── apps.py #应用入口
│   ├── __init__.py #python项目入口（空文件）
│   ├── migrations #本地数据
│   │   ├── 0001_initial.py 
│   │   ├── 0002_auto_20190213_2106.py 
│   │   ├── __init__.py
│   ├── models.py #模型
│   ├── poem_api.py #功能模块，实现诗词爬取功能
│   ├── tests.py #暂时无用
│   ├── urls.py #二级路由配置文件
│   └── views.py #视图
├── db.sqlite3 #sqlite3数据库文件
├── manage.py #调试时的主控制文件
├── media #上传/下载目录
│   └── upload
│       └── 2019
│           └── 02
│               └── 22
│                   └── u5233808181369404823fm26gp0.jpg
├── mysite #站点配置层
│   ├── __init__.py #同上
│   ├── mysql.cnf #远程数据库信息配置（暂时无用）
│   ├── settings.py #全站配置文件
│   ├── urls.py #主路由（一级路由）
│   └── wsgi.py #wsgi部署文件
├── README.md #本文档
├── static #静态文件
│   ├── css
│   │   ├── about.css
│   ├── img
│   │   ├── avatar.jpg
│   └── js
└── templates #模板层
    └── index.html
```
`pip3 install django==2.1 requests`


`python manage.py migrate `

`python manage.py makemigration`




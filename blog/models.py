from django.db import models

# Create your models here.
class Author(models.Model):
    """博客作者模型"""
    authorname = models.CharField(max_length=20)
    email = models.EmailField()
    descript = models.TextField()
    def __str__(self):
        return str(self.authorname)#命令行管理db时的输出格式   
    class Meta:
        verbose_name = '作者'
        verbose_name_plural = '作者'

class Tag(models.Model):
    """博客分类"""
    tag_name=models.CharField(max_length=20)
    create_time=models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return str(self.tag_name)
    class Meta: 
        verbose_name = '标签'
        verbose_name_plural = '标签'

class Blog(models.Model):
    """博客"""
    caption = models.CharField(max_length=50)
    author = models.ForeignKey(Author,on_delete=(False))  #一对一外键，关联作者模型
    tags = models.ManyToManyField(Tag,blank=True) #多对多字段，绑定下面的Tag模型
    content = models.TextField()  #Text长文本字段，可以写很多内容
    
    publish_time = models.DateTimeField(auto_now_add=True) #日期，新增自动写入
    update_time = models.DateTimeField(auto_now=True) #日期，修改自动更新
    recommend = models.BooleanField(default=False) #布尔字段，我用于标记是否是推荐博文
 
    def __str__(self):
        return str(self.caption)
 
    class Meta:
        #排序
        ordering=['-publish_time']
        verbose_name = '文章'
        verbose_name_plural = '文章'


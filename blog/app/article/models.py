from django.db import models

# Create your models here.
from django.db import models
from ckeditor.fields import RichTextField

from blog.app.user.models import User


class Category(models.Model):
    name = models.CharField("类别名称")
    create_time = models.DateTimeField("创建时间", auto_now_add=True)
    update_time = models.DateTimeField("修改使劲按", auto_now=True)


class Article(models.Model):
    title = models.CharField(verbose_name="标题")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL)
    content = RichTextField(verbose_name="文章内容")
    author = models.ForeignKey(User, on_delete=models.SET_NULL)
    create_time = models.DateTimeField("创建时间", auto_now_add=True)
    update_time = models.DateTimeField("修改使劲按", auto_now=True)

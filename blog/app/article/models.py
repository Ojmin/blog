from django.db import models

# Create your models here.

from django.db import models
from ckeditor.fields import RichTextField
from blog.app.user.models import User


class Article(models.Model):
    CHOICE = (("blog", "博客"), ("article", "文章",))
    title = models.CharField(verbose_name="标题", max_length=64)
    category = models.CharField(verbose_name='分类', choices=CHOICE, max_length=64)
    content = RichTextField(verbose_name="文章内容")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    is_delete = models.BooleanField(verbose_name="是否删除")
    create_time = models.DateTimeField("创建时间", auto_now_add=True)
    update_time = models.DateTimeField("修改时间", auto_now=True)

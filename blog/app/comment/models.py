from django.db import models

# Create your models here.
from django.db import models

from blog.app.article.models import Article
from blog.app.user.models import User


class Comment(models.Model):
    content = models.CharField(verbose_name="评论内容")
    article = models.ForeignKey(Article, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, on_delete=models.SET_NULL)
    create_time = models.DateTimeField("创建时间", auto_now_add=True)
    update_time = models.DateTimeField("修改使劲按", auto_now=True)

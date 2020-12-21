from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser


# AbstractBaseUser 是基本骨架，只有 3 个项： password, last_login, is_active。
from blog.app.article.models import Article


class User(AbstractUser):
    name = models.CharField(verbose_name="用户名", max_length=64)
    loving_user = models.ManyToManyField('User', verbose_name="关注的人", null=True, blank=True)
    loved_user = models.ManyToManyField('User', verbose_name="被谁关注", null=True, blank=True)
    loving_article = models.ManyToManyField(Article, verbose_name="喜欢的文章", null=True, blank=True)
    create_time = models.DateTimeField("创建时间", auto_now_add=True)
    update_time = models.DateTimeField("修改使劲按", auto_now=True)

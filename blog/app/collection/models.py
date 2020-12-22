from django.db import models
from blog.app.article.models import Article
from blog.app.user.models import User


# Create your models here.
class Collection(models.Model):
    user = models.ForeignKey('User', verbose_name="用户", on_delete=models.CASCADE)
    article = models.ForeignKey('Article', verbose_name="文章", on_delete=models.CASCADE)

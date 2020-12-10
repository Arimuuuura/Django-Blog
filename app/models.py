from django.db import models
from django.conf import settings
from django.utils import timezone

class Post(models.Model): # 投稿記事のDB
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # 投稿者, on_delete は投稿者が削除されたら記事も削除される
    title = models.CharField("タイトル", max_length=200)
    content = models.TextField("本文")
    created = models.DateTimeField("作成日", default=timezone.now)

    def __str__(self): # str 関数を作成することで、管理画面で表示される文字列を定義することができる
        return self.title
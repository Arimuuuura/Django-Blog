from django.contrib import admin
from .models import Post # 作った models.py を読み込む

admin.site.register(Post) # register 関数を使用して model を追加
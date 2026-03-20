from django.contrib import admin
from .models import Post, User # 同時匯入這兩個

admin.site.register(Post)
admin.site.register(User)
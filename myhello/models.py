from django.db import models

# 1. 這是剛才練習的 Post 資料表
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    photo = models.URLField(blank=True)
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# 2. 這是作業/後續練習需要的 User 資料表
class User(models.Model):
    user_id = models.CharField(max_length=150)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    last_login = models.DateTimeField(auto_now_add=True)
    picture = models.CharField(max_length=2048)

    def __str__(self):
        return self.first_name
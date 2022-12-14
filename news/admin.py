from django.contrib import admin
from .models import Post, Category, Article, Comment
# Register your models here.

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Article)
admin.site.register(Comment)

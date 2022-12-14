from .models import Post, Article, Comment
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ["id", "title", "desc", "img", "cat_id"]


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ["id", "author", "desc", "date"]

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
from .models import Post, Article, Comment
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ["id", "title", "desc", "img", "about", "date", "cat_id"]


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ["id", "title", "author", "desc", "date"]

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "name", "comment", "date", "artticle"]
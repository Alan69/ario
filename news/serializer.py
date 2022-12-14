<<<<<<< HEAD
from .models import Post, Article, Comment
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    desc = serializers.SerializerMethodField()

    def get_desc(self, instance):
        return str(instance.desc.html)
    
    class Meta:
        model = Post
        fields = ["id", "title", "desc", "img", "cat_id"]


class ArticleSerializer(serializers.ModelSerializer):
    desc = serializers.SerializerMethodField()

    def get_desc(self, instance):
        return str(instance.desc.html)

    class Meta:
        model = Article
        fields = ["id", "author", "desc", "date"]

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
=======
from .models import Post, Article, Comment
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
>>>>>>> ae24838919602f6967e2b9720be28cac4d9e3380
        fields = '__all__'
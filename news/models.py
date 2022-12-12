from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    desc = models.TextField(null=True, blank=True)
    img = models.ImageField(null=True, blank=True, upload_to='pics')
    cat_id = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

class Article(models.Model):
    title = models.CharField(max_length=55,  null=True, blank=True)
    author = models.CharField(max_length=55,  null=True, blank=True)
    desc = models.TextField(null=True, blank=True)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
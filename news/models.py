from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    cat_id = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


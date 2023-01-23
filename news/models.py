from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Категорий"

class Post(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True, verbose_name="Заголовок")
    about = models.TextField(null=True, blank=True, verbose_name="Под заголовок")
    desc = RichTextField(null=True, blank=True, verbose_name="Текст")
    img = models.ImageField(null=True, blank=True, upload_to='pics', verbose_name="Изображение")
    date = models.DateField(null=True, blank=True)
    cat_id = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name="Категория")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name="Новость"
        verbose_name_plural = "Новости"

class Article(models.Model):
    title = models.CharField(max_length=55,  null=True, blank=True, verbose_name="Заголовок")
    author = models.CharField(max_length=55,  null=True, blank=True, verbose_name="Автор")
    desc = RichTextField(null=True, blank=True, verbose_name="Текст")
    date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name="Статья"
        verbose_name_plural = "Статьи"

class Comment(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    date = models.DateField(auto_now=True)
    artticle = models.ForeignKey(Article, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name="Комментарий"
        verbose_name_plural = "Комментарий"
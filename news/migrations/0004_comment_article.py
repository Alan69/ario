# Generated by Django 4.1.1 on 2022-12-14 09:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_alter_article_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='article',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='news.article'),
        ),
    ]

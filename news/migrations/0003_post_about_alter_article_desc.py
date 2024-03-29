# Generated by Django 4.1.4 on 2022-12-19 06:56

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0002_alter_post_desc"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="about",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="article",
            name="desc",
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]

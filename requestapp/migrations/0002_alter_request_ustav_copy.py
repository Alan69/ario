# Generated by Django 4.1.4 on 2022-12-09 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("requestapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="request",
            name="ustav_copy",
            field=models.FileField(blank=True, null=True, upload_to="media/files"),
        ),
    ]

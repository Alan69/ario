# Generated by Django 4.1.4 on 2023-01-18 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("urequest", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="urequest",
            name="payment_check",
            field=models.FileField(blank=True, null=True, upload_to="media/files"),
        ),
        migrations.AlterField(
            model_name="urequest",
            name="udostoverenie",
            field=models.FileField(blank=True, null=True, upload_to="media/files"),
        ),
    ]

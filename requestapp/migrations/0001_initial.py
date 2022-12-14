# Generated by Django 4.1.1 on 2022-12-14 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ur_name', models.CharField(max_length=255)),
                ('biin', models.CharField(max_length=50)),
                ('fio', models.CharField(max_length=255)),
                ('job_title', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('number', models.CharField(max_length=20)),
                ('city_number', models.CharField(max_length=20)),
                ('ur_adres', models.CharField(max_length=255)),
                ('post_adres', models.CharField(max_length=255)),
                ('post_index', models.CharField(max_length=255)),
                ('ustav_copy', models.FileField(blank=True, null=True, upload_to='media/files')),
            ],
        ),
        migrations.CreateModel(
            name='RequestTypeTwo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_location', models.CharField(max_length=255)),
                ('job_title', models.CharField(max_length=255)),
                ('surname', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('father_name', models.CharField(max_length=255)),
                ('number', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=255)),
                ('adres', models.CharField(max_length=255)),
                ('cvalification', models.CharField(max_length=255)),
                ('udostoverenie', models.FileField(blank=True, null=True, upload_to='files')),
                ('diplom', models.FileField(blank=True, null=True, upload_to='files')),
                ('udostoverenie_category', models.FileField(blank=True, null=True, upload_to='files')),
                ('dok_staj', models.FileField(blank=True, null=True, upload_to='files')),
                ('comment', models.CharField(max_length=255)),
                ('prolojenie', models.FileField(blank=True, null=True, upload_to='files')),
            ],
        ),
    ]

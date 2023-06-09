# Generated by Django 4.1.7 on 2023-03-15 15:40

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='about/')),
                ('title', models.CharField(max_length=250)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField()),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='blogs/')),
                ('title', models.CharField(max_length=250)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='clases/')),
                ('title', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=150)),
                ('age', models.CharField(max_length=150)),
                ('groups', models.CharField(max_length=150)),
                ('time', models.CharField(max_length=30)),
                ('money', models.CharField(max_length=155)),
            ],
        ),
        migrations.CreateModel(
            name='Class2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=250)),
                ('name', models.CharField(max_length=250)),
                ('subject', models.CharField(max_length=255)),
                ('massage', models.TextField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='gallerys/')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='teacher/')),
                ('title', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=150)),
                ('description2', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=150)),
                ('tw', models.CharField(blank=True, max_length=255, null=True)),
                ('fac', models.CharField(blank=True, max_length=255, null=True)),
                ('In', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]

# Generated by Django 3.0.1 on 2019-12-26 17:25

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_auto_20191226_1205'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='greyhound',
            name='photo_path',
        ),
        migrations.AddField(
            model_name='boardmember',
            name='profile_image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
        migrations.AddField(
            model_name='greyhound',
            name='profile_image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='greyhound',
            name='is_spotlight',
            field=models.TextField(null=True),
        ),
    ]

# Generated by Django 3.0.1 on 2020-01-07 18:22

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20191229_1340'),
    ]

    operations = [
        migrations.AddField(
            model_name='tribute',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='tribute',
            name='profile_image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
        migrations.AddField(
            model_name='tribute',
            name='year_lost',
            field=models.CharField(default=2000, max_length=4),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.0.1 on 2019-12-20 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20191210_1419'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='end_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='host',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='start_time',
            field=models.DateTimeField(null=True),
        ),
    ]

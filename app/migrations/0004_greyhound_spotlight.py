# Generated by Django 2.2.7 on 2019-11-29 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_event_tribute'),
    ]

    operations = [
        migrations.AddField(
            model_name='greyhound',
            name='spotlight',
            field=models.BooleanField(default=False),
        ),
    ]

# Generated by Django 4.1.2 on 2022-11-28 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hashtags', '0001_initial'),
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='hashtags',
            field=models.ManyToManyField(to='hashtags.hashtag'),
        ),
    ]

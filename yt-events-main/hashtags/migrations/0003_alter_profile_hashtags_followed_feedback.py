# Generated by Django 4.1.2 on 2022-11-29 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hashtags', '0002_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='hashtags_followed',
            field=models.ManyToManyField(blank=True, to='hashtags.hashtag'),
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(choices=[('IP', 'Intellectual Property Violation'), ('VODO', 'Violence or Dangerous organizations'), ('BOH', 'Bullying or Harassment')], max_length=200)),
                ('hashtag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hashtags.hashtag')),
            ],
        ),
    ]

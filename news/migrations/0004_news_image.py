# Generated by Django 3.2.24 on 2024-02-17 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_news_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='image',
            field=models.ImageField(default='news/default.jpg', upload_to='news/'),
        ),
    ]

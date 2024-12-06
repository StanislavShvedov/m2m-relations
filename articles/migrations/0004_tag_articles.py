# Generated by Django 5.1.4 on 2024-12-05 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_remove_tag_articles'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='articles',
            field=models.ManyToManyField(related_name='tags', through='articles.Scope', to='articles.article'),
        ),
    ]

# Generated by Django 5.1.4 on 2024-12-05 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_alter_article_options_tag_scope'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='articles',
        ),
    ]

# Generated by Django 5.1.4 on 2024-12-05 14:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_tag_articles'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scopes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_main', models.BooleanField()),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scopes', to='articles.article')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scopes', to='articles.tag')),
            ],
        ),
        migrations.AlterField(
            model_name='tag',
            name='articles',
            field=models.ManyToManyField(related_name='tags', through='articles.Scopes', to='articles.article'),
        ),
        migrations.DeleteModel(
            name='Scope',
        ),
    ]

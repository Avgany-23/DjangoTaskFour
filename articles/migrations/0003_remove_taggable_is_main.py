# Generated by Django 5.1.1 on 2024-09-26 20:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_taggable_articlestags_article_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taggable',
            name='is_main',
        ),
    ]

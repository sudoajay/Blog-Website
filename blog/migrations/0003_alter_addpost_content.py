# Generated by Django 4.2 on 2023-04-14 05:12

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_addpost_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addpost',
            name='content',
            field=tinymce.models.HTMLField(null=True),
        ),
    ]

# Generated by Django 3.1 on 2020-08-16 05:57

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20200816_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myblog',
            name='myBlog_content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]

# Generated by Django 4.2.4 on 2023-08-15 20:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0003_category_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='parent_id',
        ),
        migrations.RemoveField(
            model_name='post',
            name='parent_id',
        ),
        migrations.RemoveField(
            model_name='post_comment',
            name='parent_id',
        ),
    ]

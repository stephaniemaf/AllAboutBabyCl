# Generated by Django 3.2.23 on 2024-03-28 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_comment_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='email',
        ),
    ]

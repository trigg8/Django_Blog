# Generated by Django 4.0.3 on 2022-04-09 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0014_comment_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='name',
        ),
    ]
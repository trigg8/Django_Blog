# Generated by Django 4.0.3 on 2022-04-09 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0013_remove_comment_name_comment_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='name',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
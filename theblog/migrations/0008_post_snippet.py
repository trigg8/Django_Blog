# Generated by Django 4.0.3 on 2022-04-08 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0007_alter_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Default Snippet', max_length=255),
        ),
    ]

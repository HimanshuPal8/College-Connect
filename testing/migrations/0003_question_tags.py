# Generated by Django 3.1.6 on 2021-04-09 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0002_comment_downvote_upvote'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='tags',
            field=models.TextField(default=''),
        ),
    ]
# Generated by Django 3.1.6 on 2021-05-11 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0010_auto_20210511_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='pdf',
            field=models.FileField(upload_to='notes/pfds'),
        ),
    ]

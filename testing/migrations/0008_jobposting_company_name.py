# Generated by Django 3.1.6 on 2021-05-06 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0007_auto_20210506_1025'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobposting',
            name='Company_Name',
            field=models.CharField(default='', max_length=100),
        ),
    ]

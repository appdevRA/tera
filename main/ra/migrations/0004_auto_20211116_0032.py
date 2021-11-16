# Generated by Django 3.2.6 on 2021-11-15 16:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ra', '0003_auto_20211116_0017'),
    ]

    operations = [
       
        migrations.AlterField(
            model_name='bookmarks',
            name='dateAccessed',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 16, 0, 32, 22, 524755)),
        ),
        migrations.AlterField(
            model_name='bookmarks',
            name='dateAdded',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 16, 0, 32, 22, 524755)),
        ),
        migrations.AlterField(
            model_name='bookmarks',
            name='edition',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='bookmarks',
            name='numOfCitation',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='bookmarks',
            name='numOfDownload',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='bookmarks',
            name='numOfPages',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='bookmarks',
            name='publisher',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='practice',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 16, 0, 32, 22, 526754)),
        ),
    ]

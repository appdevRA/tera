# Generated by Django 3.2.8 on 2022-02-03 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ra', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admin',
            name='department',
        ),
        migrations.AlterField(
            model_name='bookmark',
            name='folders',
            field=models.ManyToManyField(blank=True, to='ra.Folder'),
        ),
        migrations.AlterModelTable(
            name='bookmark',
            table='Bookmark',
        ),
    ]

# Generated by Django 3.2.8 on 2022-01-23 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ra', '0003_siteexception_link'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SiteException',
            new_name='Site_exception',
        ),
        migrations.AlterModelTable(
            name='site_exception',
            table='Site_exception',
        ),
    ]
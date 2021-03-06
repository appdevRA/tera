# Generated by Django 3.1.1 on 2021-05-08 04:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ra', '0004_auto_20201214_1128'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Citations',
        ),
        migrations.AddField(
            model_name='articles',
            name='date_uploaded',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='folders',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ra.user'),
        ),
    ]

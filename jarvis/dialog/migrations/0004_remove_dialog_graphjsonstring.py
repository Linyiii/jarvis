# Generated by Django 2.2.5 on 2019-10-04 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dialog', '0003_auto_20191004_1117'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dialog',
            name='graphJsonString',
        ),
    ]

# Generated by Django 3.2.8 on 2021-11-07 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_rename_registering_registerings'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='registerings',
            new_name='registering',
        ),
    ]

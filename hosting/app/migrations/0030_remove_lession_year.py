# Generated by Django 3.2.8 on 2021-11-16 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0029_auto_20211116_2154'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lession',
            name='year',
        ),
    ]
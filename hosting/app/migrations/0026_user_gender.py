# Generated by Django 3.2.8 on 2021-11-16 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(default='O', max_length=1),
        ),
    ]

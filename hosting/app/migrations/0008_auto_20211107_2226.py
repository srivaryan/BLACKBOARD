# Generated by Django 3.2.8 on 2021-11-07 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_remove_registering_confirm_your_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='registering',
            name='branch',
            field=models.CharField(default='CSE', max_length=3),
        ),
        migrations.AddField(
            model_name='registering',
            name='confirm_your_password',
            field=models.CharField(default=' ', max_length=20),
        ),
        migrations.AlterField(
            model_name='registering',
            name='password',
            field=models.CharField(max_length=20),
        ),
    ]

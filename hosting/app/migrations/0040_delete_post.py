# Generated by Django 3.2.8 on 2021-11-17 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0039_auto_20211117_0135'),
    ]

    operations = [
        migrations.DeleteModel(
            name='post',
        ),
    ]
    # operations = [
    #     migrations.RemoveField(
    #         model_name='post',
    #         name='email_id',
    #     ),
    # ]

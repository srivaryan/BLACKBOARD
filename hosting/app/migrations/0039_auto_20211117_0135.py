# Generated by Django 3.2.8 on 2021-11-16 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0038_auto_20211117_0128'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='email',
            new_name='user_id',
        ),
        # migrations.RemoveField(
        #     model_name='post',
        #     name='username',
        # ),
    ]

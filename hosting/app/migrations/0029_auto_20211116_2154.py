# Generated by Django 3.2.8 on 2021-11-16 16:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0028_lession_linklession'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lession',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='lession',
            name='password',
        ),
        migrations.RemoveField(
            model_name='linklession',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='linklession',
            name='password',
        ),
        migrations.AddField(
            model_name='lession',
            name='year',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]

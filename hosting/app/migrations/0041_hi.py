# Generated by Django 3.2.8 on 2021-11-17 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0040_delete_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='hi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=11)),
            ],
        ),
    ]
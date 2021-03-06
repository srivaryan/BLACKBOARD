# Generated by Django 3.2.8 on 2021-11-16 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0027_remove_user_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='lession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('day', models.CharField(max_length=10)),
                ('subject_id', models.CharField(max_length=6)),
                ('gmeet_link', models.CharField(max_length=1000)),
                ('period_no', models.IntegerField()),
                ('teacher_name', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='linklession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('time', models.CharField(max_length=20)),
                ('period_no', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.lession')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

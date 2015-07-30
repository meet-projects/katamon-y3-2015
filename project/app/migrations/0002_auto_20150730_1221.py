# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('date', models.DateTimeField()),
                ('address', models.CharField(max_length=60)),
                ('description', models.CharField(max_length=300)),
            ],
        ),
        migrations.DeleteModel(
            name='Events',
        ),
        migrations.RemoveField(
            model_name='account',
            name='birthday',
        ),
        migrations.RemoveField(
            model_name='account',
            name='emailAddress',
        ),
        migrations.RemoveField(
            model_name='account',
            name='name',
        ),
        migrations.RemoveField(
            model_name='account',
            name='password',
        ),
        migrations.AddField(
            model_name='account',
            name='account',
            field=models.OneToOneField(default=0, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='accounts',
            field=models.ManyToManyField(to='app.Account'),
        ),
    ]

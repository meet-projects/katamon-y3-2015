# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20150730_1324'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddEvent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('time', models.CharField(max_length=255)),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('number', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('website', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='time',
            field=models.CharField(default=datetime.datetime(2015, 8, 3, 10, 26, 4, 740931, tzinfo=utc), max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='organization',
            name='event',
            field=models.ManyToManyField(to='app.Event'),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('emailAddress', models.EmailField(unique=True, max_length=254)),
                ('password', models.CharField(max_length=30)),
                ('isPalestinian', models.BooleanField()),
                ('birthday', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('date', models.DateTimeField()),
                ('address', models.CharField(max_length=60)),
                ('description', models.CharField(max_length=300)),
            ],
        ),
    ]

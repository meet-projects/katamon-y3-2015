# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_merge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organization',
            name='password',
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='message',
            name='message',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='organization',
            name='description',
            field=models.CharField(max_length=255),
        ),
    ]

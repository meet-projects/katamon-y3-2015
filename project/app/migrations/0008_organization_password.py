# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20150803_1532'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='password',
            field=models.CharField(default=123, max_length=10),
            preserve_default=False,
        ),
    ]
